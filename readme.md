# 構築
* Python3, Docker, PostgreSQLのインストール
* .envを用意(env.templateを参照):<br>
    * db/.env
    * ir_server_api/.env(空)
    * ir_server_api/config/.env
* docker-compose build
* docker-compose up
* docker-compose run api python manage.py makemigrations
* docker-compose run api python manage.py migrate
* docker-compose run api python manage.py collectstatic

# 起動方法
* docker-compose up

# このプロジェクトの他のリポジトリ
* Front: https://github.com/MinoruIshihara/pi_ir_viewer
* Client: https://github.com/MinoruIshihara/pi_ir