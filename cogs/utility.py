import discord
from discord.ext import commands
from main import p

class Utility(commands.Cog):
	global p

	def __init__(self, client):
		self.client = client

	# When the cog is loaded
	@commands.Cog.listener()
	async def on_ready(self):
		print(f'[LOGS] {self.__class__.__name__} cog has been loaded.\n')

	# Count command
	@commands.command(name='count', aliases=['Count', 'COUNT'], description='Counts the number of words in the given `text`.')
	async def count(self, ctx, *, text):
		words = text.split()
		number_of_words = len(words)

		if number_of_words == 1:
			await ctx.reply(f'There is {number_of_words} in this text.\n*smh you can count that much yourself, why use me?*')
		else:
			await ctx.reply(f'There are {number_of_words} words in this text.')
			print(f'[LOGS] Command used: {p}count')

	# Binary command
	@commands.command(name='binary', aliases=['Binary', 'BINARY'], description='Converts the given `input` to ASCII binary.')
	async def binary(self, ctx, *, input):
		res = ''.join(format(ord(i), '08b') for i in input)
		output = str(res)

		await ctx.send(output)
		print(f'[LOGS] Command used: {p}binary')

	# Convert command
	@commands.command(name='convert', aliases=['Convert', 'CONVERT'], description='Converts the given `input`(which would/must be ASCII binary) to text.')
	async def convert(self, ctx, *, input):
		binary_int = int(input, 2)
		byte_number = binary_int.bit_length() + 7 // 8
		binary_array = binary_int.to_bytes(byte_number, "big")
		converted_text = binary_array.decode()

		await ctx.send(converted_text)
		print(f'[LOGS] Command used : {p}convert')

	# Reverse command
	@commands.command(name='reverse', aliases=['r', 'R', 'Reverse', 'REVERSE', 'esrever', 'ESREVER', 'Esrever'], description='Reverses the given text.')
	async def reverse(self, ctx, *, text):
		'''Reverses the given input(text).'''
		reversedString = ''

		for letter in text:
			reversedString = letter + reversedString

		await ctx.send(reversedString)
		print(f'[LOGS] Command used: {p}reverse')

	# Calculate command
	@commands.command(name='calculate', aliases=['Calculate', 'CALCULATE', 'c', 'C', 'calc', 'Calc', 'CALC', 'cal', 'Cal', 'CAL'], description='Evaluates the given input.\n`.help calc` for more info.')
	async def calculate(self, ctx, *, input):
		'''Evaluates the given input'''
		await ctx.send(eval(input))
		print(f'[LOGS] Command used: {p}calculate')

	# Uppercase command
	@commands.command(name='uppercase', aliases=['Uppercase', 'UPPERCASE', 'upper', 'Upper', 'UPPER'], description='Converts the given text to UPPERCASE.')
	async def uppercase(slef, ctx, *, text):
		'''Converts given input to uppercase'''
		await ctx.reply(text.upper())
		print(f'[LOGS] Command used: {p}upper')

	# Lowercase command
	@commands.command(name='lowercase', aliases=['Lowercase', 'LOWERCASE', 'lower', 'Lower', 'LOWER'], description='Converts the given text to lowercase.')
	async def lowercase(slef, ctx, *, text):
		'''Converts given input to lowercase'''
		await ctx.reply(text.lower())
		print(f'[LOGS] Command used: {p}lower')

def setup(client):
	client.add_cog(Utility(client))
