import os, sys, random, discord, subprocess, time, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes, urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, asyncio, functools, logging; from colorama import Fore; from discord.ext import commands
title = open('./system/title').read(); motd = open('./system/motd').readlines(); print(f'{Fore.RED}{title}\n{Fore.BLUE}Message Of the Day: {Fore.GREEN}{random.choice(motd)}'+Fore.RESET)
with open('./settings/config.json') as conf:   config = json.load(conf); token = config.get('token'); prefix = config.get('prefix') #addmore=l8r
class demonic0(discord.Client):

    async def on_ready(self):
        print(f'{Fore.BLUE}{self.user}{Fore.GREEN} has been connected to Discord!')
if token != '':
    print(f'{Fore.GREEN}Starting Up....'+Fore.RESET)
    CLIENT = demonic0()
    CLIENT.run(token, bot=False)
else:
    print(f'{Fore.RED}[ERROR] config file invalid')
