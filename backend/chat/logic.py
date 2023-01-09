def verification_msg(msg):
	if msg == "" or len(msg) > 512:
		return False

	return True