import os, json
from requests import get

from .util import *
from flask import Blueprint, request, url_for, redirect, render_template, flash
pvsdata = Blueprint('pvsdata', __name__, template_folder="templates/pvsdata")


data_folder = os.path.join(os.path.abspath(os.path.dirname(os.path.abspath(__file__))), "data")

NA_Version = get("https://ddragon.leagueoflegends.com/realms/na.json").json()['v']
NA_Champs = get(f"https://ddragon.leagueoflegends.com/cdn/{NA_Version}/data/en_US/champion.json").json()
ChampKey = {}
ChampImage = {}

for champ in NA_Champs['data'].values():
	ChampKey[champ['key']] = champ['id']
	ChampImage[champ['key']] = champ['image']['full']

def get_phase_data_loc(phase_id, get_location = False, prefix=None):
	location = os.path.join(data_folder, "leagues")

	if prefix:
		location = os.path.join(prefix, *location.split("/"))
	
	for phase_file in os.listdir(location):
		if phase_id in phase_file:
			if get_location:
				return os.path.join(location, phase_file)
			return True
	return False

@pvsdata.route("/")
def show_phase_general():
	general_data = os.path.join(data_folder, "leagues", "_GENERAL_DATA.json")
	print("Started")
	league_id = "f70fa8cf-059d-4d4b-8aeb-a57c9757edce"
	season_id = "665a9878-a0d8-4756-9a8e-e2f5fefe51f6"
	phase_id =  "05c5f2a4-3bea-4738-af77-c0d6600fae06"


	with open(get_phase_data_loc(phase_id, True), 'r') as PHASE_RAW:
		phase_data = json.load(PHASE_RAW)
	print("Phase data pulled")	

	all_members = []

	for team in phase_data['teams'].values():
		all_members.extend(team['memberAvgStats'])

	return render_template("ranking_chart.html", **{
		"mpc": phase_data['phaseMPC'],
		"ChampKey": ChampKey,
		"rankings": phase_data['rankings'],
		"round": round,
		"memberAvgStats": all_members,
	})


@pvsdata.route("/team/<team_id>/")
def show_team_data(team_id):
	general_data = os.path.join(data_folder, "leagues", "_GENERAL_DATA.json")
	print("Started")
	phase_id =  "05c5f2a4-3bea-4738-af77-c0d6600fae06"


	with open(get_phase_data_loc(phase_id, True), 'r') as PHASE_RAW:
		phase_data = json.load(PHASE_RAW)

	team_data = phase_data['teams'][team_id]

	return render_template("team_chart.html", **{
		"teamData": team_data,
		"mpc": team_data['teamMPC'],
		"ChampKey": ChampKey,
		"zip_fill_none": zip_fill_none,
		"ddragon_patch_url": "https://ddragon.leagueoflegends.com/cdn/" + NA_Version,
		"str": str,
		"int": int,
		"round": round,
	})
	

@pvsdata.route("/game/<team_id>/<game_id>/")
def show_game_data(team_id, game_id):
	with open(os.path.join(data_folder, "mlp.json"), 'r') as mlp_raw:
		mlp = json.load(mlp_raw)
	print("Started")
	phase_id =  "05c5f2a4-3bea-4738-af77-c0d6600fae06"


	with open(get_phase_data_loc(phase_id, True), 'r') as PHASE_RAW:
		phase_data = json.load(PHASE_RAW)

	team_data = phase_data['teams'][team_id]

	game_data = None
	for game in team_data['games']:
		if game['gameId'] == game_id:
			game_data = game

	all_players = []
	if game_data['teamGameStats'] != []:
		all_players.extend(game_data['teamGameStats'][0]["readdedPlayerGameStats"])
		all_players.extend(game_data['teamGameStats'][1]["readdedPlayerGameStats"])

	return render_template("full_game.html", **{
		"gameData": game_data,
		"ChampKey": ChampKey,
		"zip_fill_none": zip_fill_none,
		"ddragon_patch_url": "https://ddragon.leagueoflegends.com/cdn/" + NA_Version,
		"ddragon_base_url": "https://ddragon.leagueoflegends.com/cdn",
		"str": str,
		"int": int,
		"round": round,
		"len": len,
		"mlp": mlp,
		"get_largest_key_from_list_of_dicts": get_largest_key_from_list_of_dicts,
		"all_players": all_players,
	})


@pvsdata.app_errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404