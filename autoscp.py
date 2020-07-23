import pexpect
import sys
import time

class AutoScp:
	def __init__(self, hfile, tfile, pwd):
		self.child = pexpect.spawn(f'scp -r {hfile} {tfile}')
		self.child.logfile = sys.stdout.buffer
		res = self.child.expect([pexpect.TIMEOUT, 'password'])
		if res == 1:
			self.child.sendline(f'{pwd}')
			res = self.child.expect([pexpect.TIMEOUT, 'permission denied', '100'])
			if res == 2:
				print('Done')
			else:
				sys.exit('Failed this shit')
		else:
			sys.exit('Password prompt not received')


if __name__ == '__main__':
	if len(sys.argv) < 4:
		print(f'Usage : {sys.argv[0]} <host filepath> <target filepath> <target password>')
		sys.exit(1)

	AutoScp(sys.argv[1], sys.argv[2], sys.argv[3])
