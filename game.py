from up_down import UpDown

ud=UpDown()

def new_game(d):
	try:
		count = int(d.get('count', [''])[0])
	except:
		return {'code': 'error', 'msg': 'count not given'}

	ud.newGame(count)

	return {'code': 'success'}


def updown(d):
	try:
		updown = int(d.get('updown', [''])[0])
	except:
		return {'code': 'error', 'msg': 'wrong guess parameter'}

	answer = ud. updown(updown)

	return {'code': 'success', 'answer': answer, 'trials': trials}
