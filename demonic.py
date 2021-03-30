import os, sys, random, discord, subprocess, time, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes, urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, asyncio, functools, logging; from colorama import Fore
title = open('./system/title').read(); motd = open('./system/motd').readlines(); print(f'''{Fore.RED}{title}\n{Fore.CYAN}Message Of the Day:''',Fore.GREEN+random.choice(motd)+Fore.RESET)
with open('./settings/config.json') as conf:   config = json.load(conf); token = config.get('token'); prefix = config.get('prefix') #addmore=l8r
print(token, prefix)
