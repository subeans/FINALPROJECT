from strikeball import StrikeBall

sb = StrikeBall()

def new_game(d):
	try:
		count = int(d.get('count', [''])[0])
	except:
		return {'code': 'error', 'msg': 'count not given'}

	sb.newGame(count)

	return {'code': 'success'}


def guess(d):
	try:
		guess = d.get('guess', [''])[0]
	except:
		return {'code': 'error', 'msg': 'wrong guess parameter'}

	strikes, balls = sb.guess(guess)
	trials = sb.getGuessCount()

	return {'code': 'success', 'strikes': strikes, 'balls': balls, 'trials': trials}
