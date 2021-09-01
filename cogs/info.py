import discord
from discord.ext import commands
from main import p
from main import client

class Info(commands.Cog):
	global p

	def __init__(self, client):
		self.client = client

	# When the cog is loaded
	@commands.Cog.listener()
	async def on_ready(self):
		print(f'[LOGS] {self.__class__.__name__} cog has been loaded.\n')

	# Ping command
	@commands.command(name='ping', aliases=['Ping', 'PING'], description='Shows the bot\'s ping/latency.')
	async def ping(self, ctx):
		'''Tells the latency of the bot'''
		global client
		latency = round(client.latency * 1000)

		await ctx.send(f'🏓 | ...pong! In {latency}ms.')
		print(f'[LOGS] Command used: {p}ping')

	# help command
	@commands.command(name='help', aliases=['Help', 'HELP'], description='Shows help about a module or command(only certain commands). `{p}help all` for a list of all commands.')
	async def help(self, ctx, input_=None):
		'''A fully automatic help command which also shows the parameters needed for a command.'''

		# (There is probably a better, more efficient way to make commands other than if-elif-else statements.)

		if input_ != None:
			c = input_.lower()
		# help
		if input_ == None:
			embed = discord.Embed(title='Normal Bot\'s Command List', description=f'Use `{p}help [module]` for more info on a module.\nUse `{p}help all` for a list of all commands.', color=discord.Color.random())

			embed.add_field(name='🛠️Utility', value=f'`{p}help utility`')
			embed.add_field(name='😄Fun', value=f'`{p}help fun`')
			embed.add_field(name='ℹ️Info', value=f'`{p}help info`')
			embed.add_field(name='🐶Animals', value=f'`{p}help animals`')
			embed.add_field(name='🎲Games', value=f'`{p}help games`')
			embed.add_field(name='❗Moderation', value=f'`{p}help moderation`')

			await ctx.reply(embed=embed)
			print(f'[LOGS] Command used: {p}help')
		# help all
		elif c == 'all':
			'''Shows all commands'''
			embed = discord.Embed(title='List of all commands:', description=f'The bot prefix is `{p}`.', color=discord.Color.random())

			# Makes a field for every command.
			for command in self.client.walk_commands():
					parameters = list(command.params.keys())
					try:
						if parameters[2]:
							if parameters[3]:
								if parameters[4]:
									pm1 = parameters[2].replace('_', ' (optional)')
									pm2 = parameters[3].replace('_', ' (optional)')
									pm3 = parameters[4].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`> <`{pm2}`> <`{pm3}`>', value=command.description)
								else:
									pm1 = parameters[2].replace('_', ' (optional)')
									pm2 = parameters[3].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`> <`{pm2}`>', value=command.description)
							else:
								pm1 = parameters[2].replace('_', ' (optional)')

								embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
						else:
							embed.add_field(name=p + command.name, value=command.description)
					except:
						try:
							if parameters[2]:
								if parameters[3]:
									pm1 = parameters[2].replace('_', ' (optional)')
									pm2 = parameters[3].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`> <`{pm2}`>', value=command.description)
								else:
									pm1 = parameters[2].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
							else:
								embed.add_field(name=p + command.name, value=command.description)
						except:
							try:
								if parameters[2]:
									pm1 = parameters[2].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
								else:
									embed.add_field(name=p + command.name, value=command.description)
							except:
								embed.add_field(name=p + command.name, value=command.description)

			# Adding fields for sub-commands manually
			embed.add_field(name=f'{p}help `calc`', value=f'A detailed guide on how to use `{p}calculate` command.')
			embed.add_field(name=f'{p}help `hex`', value=f'Shows how to use `{p}hex` command properly and a list of all colours avaliable in `{p}hex`.')

			await ctx.reply(embed=embed)
			print(f'[LOGS] Command used: {p}help all')
		# help utility
		elif c == 'utility':
			'''Shows 'utility' commands'''
			embed = discord.Embed(description='**🛠️Utility Commands**', color=discord.Color.random())

			# Makes a field for every command in 'utility' module.
			for command in self.client.walk_commands():
				if command.module == 'cogs.utility':
					parameters = list(command.params.keys())
					try:
						if parameters[2]:
							if parameters[3]:
								if parameters[4]:
									pm1 = parameters[2].replace('_', ' (optional)')
									pm2 = parameters[3].replace('_', ' (optional)')
									pm3 = parameters[4].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} `<{pm1}`> <`{pm2}`> <`{pm3}`>', value=command.description)
								else:
									pm1 = parameters[2].replace('_', ' (optional)')
									pm2 = parameters[3].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`> <`{pm2}`>', value=command.description)
							else:
								pm1 = parameters[2].replace('_', ' (optional)')

								embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
						else:
							embed.add_field(name=p + command.name, value=command.description)
					except:
						try:
							if parameters[2]:
								if parameters[3]:
									pm1 = parameters[2].replace('_', ' (optional)')
									pm2 = parameters[3].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`> <`{pm2}`>', value=command.description)
								else:
									pm1 = parameters[2].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
							else:
								embed.add_field(name=p + command.name, value=command.description)
						except:
							try:
								if parameters[2]:
									pm1 = parameters[2].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
								else:
									embed.add_field(name=p + command.name, value=command.description)
							except:
								embed.add_field(name=p + command.name, value=command.description)

			await ctx.reply(embed=embed)
			print(f'[LOGS] Command used: {p}help utility')
		# help fun
		elif c == 'fun':
			'''Shows 'fun' commands'''
			embed = discord.Embed(description='**😄Fun Commands**', color=discord.Color.random())

			# Makes a field for every command in 'fun' module.
			for command in self.client.walk_commands():
				if command.module == 'cogs.fun':
					parameters = list(command.params.keys())
					try:
						if parameters[2]:
							if parameters[3]:
								if parameters[4]:
									pm1 = parameters[2].replace('_', ' (optional)')
									pm2 = parameters[3].replace('_', ' (optional)')
									pm3 = parameters[4].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} `<{pm1}`> <`{pm2}`> <`{pm3}`>', value=command.description)
								else:
									pm1 = parameters[2].replace('_', ' (optional)')
									pm2 = parameters[3].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`> <`{pm2}`>', value=command.description)
							else:
								pm1 = parameters[2].replace('_', ' (optional)')

								embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
						else:
							embed.add_field(name=p + command.name, value=command.description)
					except:
						try:
							if parameters[2]:
								if parameters[3]:
									pm1 = parameters[2].replace('_', ' (optional)')
									pm2 = parameters[3].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`> <`{pm2}`>', value=command.description)
								else:
									pm1 = parameters[2].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
							else:
								embed.add_field(name=p + command.name, value=command.description)
						except:
							try:
								if parameters[2]:
									pm1 = parameters[2].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
								else:
									embed.add_field(name=p + command.name, value=command.description)
							except:
								embed.add_field(name=p + command.name, value=command.description)

			await ctx.reply(embed=embed)
			print(f'[LOGS] Command used: {p}help fun')
		# help info
		elif c == 'info':
			'''Shows 'info' commands'''
			embed = discord.Embed(description='**ℹ️Info Commands**', color=discord.Color.random())

			# Makes a field for every command in 'info' module.
			for command in self.client.walk_commands():
				if command.module == 'cogs.info':
					parameters = list(command.params.keys())
					try:
						if parameters[2]:
							if parameters[3]:
								if parameters[4]:
									pm1 = parameters[2].replace('_', ' (optional)')
									pm2 = parameters[3].replace('_', ' (optional)')
									pm3 = parameters[4].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} `<{pm1}`> <`{pm2}`> <`{pm3}`>', value=command.description)
								else:
									pm1 = parameters[2].replace('_', ' (optional)')
									pm2 = parameters[3].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`> <`{pm2}`>', value=command.description)
							else:
								pm1 = parameters[2].replace('_', ' (optional)')

								embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
						else:
							embed.add_field(name=p + command.name, value=command.description)
					except:
						try:
							if parameters[2]:
								if parameters[3]:
									pm1 = parameters[2].replace('_', ' (optional)')
									pm2 = parameters[3].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`> <`{pm2}`>', value=command.description)
								else:
									pm1 = parameters[2].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
							else:
								embed.add_field(name=p + command.name, value=command.description)
						except:
							try:
								if parameters[2]:
									pm1 = parameters[2].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
								else:
									embed.add_field(name=p + command.name, value=command.description)
							except:
								embed.add_field(name=p + command.name, value=command.description)

			# Adding fields for sub-commands manually
			embed.add_field(name=f'{p}help `calc`', value=f'A detailed guide on how to use `{p}calculate` command.')
			embed.add_field(name=f'{p}help `hex`', value=f'Shows how to use `{p}hex` command properly and a list of all colours avaliable in `{p}hex`.')

			await ctx.reply(embed=embed)
			print(f'[LOGS] Command used: {p}help info')
		# help animal/animals
		elif c == 'animal' or c =='animals':
			embed = discord.Embed(description='**🐶Animals Commands**', color=discord.Color.random())

			# Makes a field for every command in 'animal/animals' module.
			for command in self.client.walk_commands():
				if command.module == 'cogs.animals':
					parameters = list(command.params.keys())
					try:
						if parameters[2]:
							if parameters[3]:
								if parameters[4]:
									pm1 = parameters[2].replace('_', ' (optional)')
									pm2 = parameters[3].replace('_', ' (optional)')
									pm3 = parameters[4].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} `<{pm1}`> <`{pm2}`> <`{pm3}`>', value=command.description)
								else:
									pm1 = parameters[2].replace('_', ' (optional)')
									pm2 = parameters[3].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`> <`{pm2}`>', value=command.description)
							else:
								pm1 = parameters[2].replace('_', ' (optional)')

								embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
						else:
							embed.add_field(name=p + command.name, value=command.description)
					except:
						try:
							if parameters[2]:
								if parameters[3]:
									pm1 = parameters[2].replace('_', ' (optional)')
									pm2 = parameters[3].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`> <`{pm2}`>', value=command.description)
								else:
									pm1 = parameters[2].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
							else:
								embed.add_field(name=p + command.name, value=command.description)
						except:
							try:
								if parameters[2]:
									pm1 = parameters[2].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
								else:
									embed.add_field(name=p + command.name, value=command.description)
							except:
								embed.add_field(name=p + command.name, value=command.description)

			await ctx.reply(embed=embed)
			print(f'[LOGS] Command used: {p}help animal(s)')
		# help game/games
		elif c == 'game' or c =='games':
				embed = discord.Embed(description='**🎲Game Commands**', color=discord.Color.random())

				# Makes a field for every command in 'game/games' module.
				for command in self.client.walk_commands():
					if command.module == 'cogs.games':
						parameters = list(command.params.keys())
						try:
							if parameters[2]:
								if parameters[3]:
									if parameters[4]:
										pm1 = parameters[2].replace('_', ' (optional)')
										pm2 = parameters[3].replace('_', ' (optional)')
										pm3 = parameters[4].replace('_', ' (optional)')

										embed.add_field(name=f'{p}{command.name} `<{pm1}`> <`{pm2}`> <`{pm3}`>', value=command.description)
									else:
										pm1 = parameters[2].replace('_', ' (optional)')
										pm2 = parameters[3].replace('_', ' (optional)')

										embed.add_field(name=f'{p}{command.name} <`{pm1}`> <`{pm2}`>', value=command.description)
								else:
									pm1 = parameters[2].replace('_', ' (optional)')

									embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
							else:
								embed.add_field(name=p + command.name, value=command.description)
						except:
							try:
								if parameters[2]:
									if parameters[3]:
										pm1 = parameters[2].replace('_', ' (optional)')
										pm2 = parameters[3].replace('_', ' (optional)')

										embed.add_field(name=f'{p}{command.name} <`{pm1}`> <`{pm2}`>', value=command.description)
									else:
										pm1 = parameters[2].replace('_', ' (optional)')

										embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
								else:
									embed.add_field(name=p + command.name, value=command.description)
							except:
								try:
									if parameters[2]:
										pm1 = parameters[2].replace('_', ' (optional)')

										embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
									else:
										embed.add_field(name=p + command.name, value=command.description)
								except:
									embed.add_field(name=p + command.name, value=command.description)

				await ctx.reply(embed=embed)
				print(f'[LOGS] Command used: {p}help game(s)')
		# help moderation
		elif c == 'moderation' or c =='mod':
					embed = discord.Embed(description='**❗Moderation Commands**', color=discord.Color.random())

					# Makes a field for every command in 'moderation' module.
					for command in self.client.walk_commands():
						if command.module == 'cogs.moderation':
							parameters = list(command.params.keys())
							try:
								if parameters[2]:
									if parameters[3]:
										if parameters[4]:
											pm1 = parameters[2].replace('_', ' (optional)')
											pm2 = parameters[3].replace('_', ' (optional)')
											pm3 = parameters[4].replace('_', ' (optional)')

											embed.add_field(name=f'{p}{command.name} `<{pm1}`> <`{pm2}`> <`{pm3}`>', value=command.description)
										else:
											pm1 = parameters[2].replace('_', ' (optional)')
											pm2 = parameters[3].replace('_', ' (optional)')

											embed.add_field(name=f'{p}{command.name} <`{pm1}`> <`{pm2}`>', value=command.description)
									else:
										pm1 = parameters[2].replace('_', ' (optional)')

										embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
								else:
									embed.add_field(name=p + command.name, value=command.description)
							except:
								try:
									if parameters[2]:
										if parameters[3]:
											pm1 = parameters[2].replace('_', ' (optional)')
											pm2 = parameters[3].replace('_', ' (optional)')

											embed.add_field(name=f'{p}{command.name} <`{pm1}`> <`{pm2}`>', value=command.description)
										else:
											pm1 = parameters[2].replace('_', ' (optional)')

											embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
									else:
										embed.add_field(name=p + command.name, value=command.description)
								except:
									try:
										if parameters[2]:
											pm1 = parameters[2].replace('_', ' (optional)')

											embed.add_field(name=f'{p}{command.name} <`{pm1}`>', value=command.description)
										else:
											embed.add_field(name=p + command.name, value=command.description)
									except:
										embed.add_field(name=p + command.name, value=command.description)

					await ctx.reply(embed=embed)
					print(f'[LOGS] Command used: {p}help moderation')
		# help hex
		elif c == 'hex':
			'''Gives information about .hex command.'''

			embed = discord.Embed(description=f'**How to use:** To use the command, simply type `{p}hex` followed by the name of the colour you want. If the colour is available, the bot will return the hex code of the colour.\n**Example:** `{p}hex red`\n\nIf your colour\'s name consists of two words, type it in one word.\n**Example:** Type `{p}hex darkgreen` instead of "{p}hex dark green".\n\nHere are all the colours available in `{p}hex`:-')

			embed.set_image(url='https://cdn.discordapp.com/attachments/878136393858187285/879052476026851398/sphx_glr_named_colors_003.png')

			await ctx.reply(embed=embed)
			print(f'[LOGS] Command used: {p}help hex')
		elif c == 'c' or c == 'calc' or c == 'calculate' or c == 'cal':
			'''Gives information about .calculate command.'''

			embed = discord.Embed(title='➕✖️➕✖️➕Calculator Commands➖➗➖➗',description=f'**Usage:** `{p}caclulate <input>`. **Example:** `{p}calculate 20+1`.',color=discord.Color.random())

			embed.add_field(name='Addition       =`X+Y`',value='**Examples:**\n`23+56`, `23+4+51`',inline=True)
			embed.add_field(name='Subtraction   =`X-Y`',value='**Examples:**\n`56-23`, `1-23-2`',inline=True)
			embed.add_field(name='Multiplication =`X*Y`',value='**Examples:**\n`3*7`, `354\*65`',inline=True)
			embed.add_field(name='Division        =`X/5`',value='**Examples:**\n`26/2`, `2352/435`',inline=True)
			embed.add_field(name='Powers         =`X**Y`',value='**Examples:**\n`2**3` (this means 2^3), `231**44` (this means 231^44',inline=True)
			embed.add_field(name='Remainder      =`X%Y`',value='**Examples:**\n`3%1` (this will give remainder of 3/1), `325%6` (this will give remainder of 325/6)',inline=True)

			embed.add_field(name='**Comparison Operators: **',value="Comparison Operators return `True` or `False` value.",inline=False)

			embed.add_field(name="Greater than(>)             ='`>`'",value="Examples: `5>4`, `234>3532`",inline=True)
			embed.add_field(name="Less than(<)                ='`<`'",value="Examples: `45<5`, `3546<567`",inline=True)
			embed.add_field(name="Equal to(=)                 ='`==`'",value="Examples: `5==4`, `3245==3425`",inline=True)
			embed.add_field(name="Not equal to(≠)             ='`!=`'",value="Examples: `53!=67`, `451!=451`",inline=True)
			embed.add_field(name="Greater than or equal to(≥) ='`>=`'",value="Examples: `54>=32`, `2>=65`",inline=True)
			embed.add_field(name="Less than or equal to(≤)    ='`<=`'",value="Examples: `34<=78`, `412<=23`",inline=True)

			embed.set_footer(text=f"⭐PROTIP: You can simply type '{p}c' instead of typing the full command name (very cool).")

			await ctx.reply(embed=embed)
			print(f'[LOGS] Command used: {p}help calc')


def setup(client):
	client.add_cog(Info(client))
