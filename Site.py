from flask import Flask, redirect, url_for;
from random import randint;
app = Flask("Very cool name");

frass = ["Кто двинется, тот гей.","Лучше 5 см спереди,\nчем учить assembler", "UTF-8 not supported","","Вы думали я забыл?\nНо нет! Я забыл.", "500 Internal Server Error", "Вова работай!","Достаём двойные листочки","-40°C"]

@app.route("/")
def ToMainPage(*_):
	return redirect(url_for("MainPage"))

@app.route("/MainPage")
def MainPage():
	return '''<!DOCTYPE html>

<head><title>Основной сайт сервера</title></head>
<body>
	<style>
		*{
			padding: 0;
			margin: 0;
		}
		.border {
			padding: 2%;
			text-align: center;
		}
		.anim {
			-webkit-animation: scale-up-hor-center 0.4s cubic-bezier(0.390, 0.575, 0.565, 1.000) both;
					animation: scale-up-hor-center 0.4s cubic-bezier(0.390, 0.575, 0.565, 1.000) both;
		}
		.gradient{background: linear-gradient(to bottom right, rgb(189, 129, 0), rgb(170, 0, 0)); background-size: cover; min-height:100vh;}
		h2{color: white}
		h1{color: whitesmoke;}
		a{color: rgb(218, 218, 255);}
		li{color: red;}
		.y{-webkit-animation:roll-in-top 5s ease-in-out infinite alternate both;animation:roll-in-top 5s ease-in-out infinite alternate both}
		@-webkit-keyframes roll-in-top{0%{-webkit-transform:translateY(-800px) rotate(-540deg);transform:translateY(-800px) rotate(-540deg);opacity:0}100%{-webkit-transform:translateY(0) rotate(0deg);transform:translateY(0) rotate(0deg);opacity:1}}@keyframes roll-in-top{0%{-webkit-transform:translateY(-800px) rotate(-540deg);transform:translateY(-800px) rotate(-540deg);opacity:0}100%{-webkit-transform:translateY(0) rotate(0deg);transform:translateY(0) rotate(0deg);opacity:1}}
		@-webkit-keyframes scale-up-hor-center {
			0% {
				-webkit-transform: scaleX(0.4);
						transform: scaleX(0.4);
			}
			100% {
				-webkit-transform: scaleX(1);
						transform: scaleX(1);
			}
			}
			@keyframes scale-up-hor-center {
			0% {
				-webkit-transform: scaleX(0.4);
						transform: scaleX(0.4);
			}
			100% {
				-webkit-transform: scaleX(1);
						transform: scaleX(1);
			}
			}
	</style>
	<div class="gradient">
		<div class="y"><h2>Жизненные фразы:\n"'''+ frass[randint(0,len(frass)-1)] +'''"</h2></div>
		<div class="border">
			<img src='https://i.pinimg.com/564x/8e/54/b1/8e54b114023bca08d4c23b620adef809.jpg' align = "right">
				<div class="anim">
					<h1>Куда надо?</h1>
					<li>
						<a href="/ChessPage">Шахматы</a>
					</li>
					<form action="/send", method="post">
						<input type="text" name="Nickname" placeholder="Ник">
						<input type="text" name="comment" placeholder="Cumментарий">
						<input type="checkbox" name="spam" value="t"> Спам
						<input type="submit" value="Отправить">
					</form>
				</div>
		</div>
		<div class="border">
			<a href="https://discord.gg/crSZCMvRbQ"><img src="https://upload.wikimedia.org/wikipedia/ru/thumb/b/b7/Discord_logo_svg.svg/2560px-Discord_logo_svg.svg.png" width="400" height="70"></a>
			<a href="https://www.youtube.com/c/TheEnG1eNbaHHbaSh_OR1G1NAJL"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/YouTube_full-color_icon_%282017%29.svg/2560px-YouTube_full-color_icon_%282017%29.svg.png" width="150" height="100"></a>
		</div>
	</div>
</body>''';

app.run("0.0.0.0",8000);