import requests, time, bs4, json

m = '\033[1;31m'
p = '\033[1;37m'
h = '\033[1;32m'
b = '\033[1;34m'

class Michabit:
	def __init__(self):
		self.index = 'https://michabitco.in/'
		self.banner = (f"""
{p}                 *****
            BOT MICHABITCO.IN
	************************

{h}@ {p}Author : https://t.me/aditia_dtz
{h}@ {p}Note : script to mining bitcoin from michabitco.in
{p}  Subscribe Dtz Cruzxt Channel 😗""")
		self.headers = {
			"Host": "michabitco.in",
			"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"User-Agent":'',
			"Cookie":'',
			}
		self.getCuki()

	def getCuki(self):
		bs4.os.system('clear')
		print(self.banner)
		print(f"""
{p} 1. Edit Headers
{p} 2. Start Bot
""")
		self.iori = int(input(f' {p}• Choice {p}: '))
		if self.iori == 1:
			self.cuki = input(f'\n {p}• Cookie {p}: ')
			self.uwa = input(f' {p}• User Agent {p}: ')
			if self.cuki and self.uwa != '':
				with open('.logs.json','w') as f:
					f.write(
						json.dumps({"cuki":self.cuki,"uwa":self.uwa})
					)
				print(f'{p} • success edit config')
				time.sleep(0.8)
				self.getCuki()
			else:
				exit(f"{p} • {m} Jangan ada yang komsong ngab!")
		elif self.iori == 2:
			if bs4.os.path.isfile('.logs.json'):
				self.j = json.loads(open('.logs.json').read())
				self.headers["Cookie"] = self.j["cuki"]
				self.headers["User-Agent"] = self.j["uwa"]
				self.login()
			else:
				exit(f"{p} • {m} Edit config sebelum start bot ngab!")
		else:
			exit(f"{p} • {m} invalid choice!")

	def waiting(self, x):
		for i in range(x,0,-1):
			bs4.sys.stdout.write("\r • {}tunggu {:2d} {}seconds!".format(p,i,h))
			bs4.sys.stdout.flush()
			time.sleep(1)

	def login(self):
		self.page = requests.get(self.index, headers=self.headers).text
		self.c = bs4.BeautifulSoup(self.page,"html.parser")
		self.user = self.c.find("div",class_="info").text.strip().split('\n')[0]
		self.balance = [''.join(y.split()[-2:]) for y in [y for y in self.c.find("div",class_="block").text.strip().split('\n') if y != ''][:2]]
		self.claim = [i for i in self.c.find("div",id="dashboard-info").text.strip().split('\n') if i != '' and 'claims' in i]
		bs4.os.system('clear')
		print(self.banner)
		print(f"""
 --------
 ~ Welcome {self.user} 👋
 ~ Account Balance : {self.balance[0]}
 ~ Current Bits : {self.balance[1]}
 ~ Claims Today : {self.claim[0]}
 ~ Claims Total : {self.claim[1]}
 -------- """)
		print(f" • start, bot run!")
		self.q = 1
		while True:
			self.token = bs4.re.search(r"var\stoken\s=\s'(.*?)'",self.page)
			if self.token is None:
				exit(f" • gagal mendapatkan token :'(")
			self.x = bs4.BeautifulSoup(self.page,"html.parser").find("span", id="claimTime")
			if self.x is not None:
				self.waiting(int(self.x.text.strip().split()[0]))
			self.headers["referer"] = self.index
			self.cl = requests.post("https://michabitco.in/system/ajax.php",data={"a":"getFaucet","token":self.token.group(1),"challenge":"false","response":"false"},headers=self.headers).json()
			if self.cl["status"] == 200:
				self.stat = " ".join(bs4.BeautifulSoup(self.cl["message"],"html.parser").text.strip().split()[1:])
				print(f'\n{p} • {h}{self.stat}{p}')
				self.headers["referer"]=''
			else:
				print(f'\n{p} • {m}gagal claim reward!')
				continue
			self.page = requests.get(self.index,headers=self.headers).text

if __name__=="__main__":
	try:
		Michabit()
	except:
		raise TypeError("Goblokkkk!")
