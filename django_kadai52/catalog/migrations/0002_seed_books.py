from django.db import migrations
from datetime import date
def seed(apps, schema_editor):
    Book = apps.get_model('catalog','Book')
    data = [
        ('Python入門','山田太郎','Programming','初心者向けのPython入門', date(2021,5,1)),
        ('Django実践','佐藤花子','Web','Djangoで作る実用Web', date(2022,3,14)),
        ('機械学習概論','鈴木一郎','AI','基礎からのML概説', date(2020,10,10)),
        ('データベース設計','高橋健','DB','正規化とクエリ最適化', date(2019,7,7)),
        ('東京ガイド','田中真','Travel','東京の見どころ', date(2023,4,2)),
        ('関西グルメ','小林優','Travel','大阪・京都の名店', date(2018,11,20)),
        ('アルゴリズム図鑑','中村さとし','CS','図解で学ぶアルゴリズム', date(2017,9,1)),
        ('フロントエンド設計','A. Tan','Web','UI設計と実装Tips', date(2024,1,15)),
        ('バックエンド設計','B. Lee','Web','API設計とテスト', date(2021,12,1)),
        ('ネットワーク基礎','C. Kim','Infra','TCP/IP入門', date(2016,6,6)),
        ('クラウドサービス入門','D. Chen','Cloud','主要クラウド比較', date(2022,9,30)),
        ('コンテナ実践','E. Park','DevOps','Dockerと運用', date(2020,1,5)),
        ('Kubernetes入門','F. Ito','DevOps','K8sの基礎', date(2023,7,19)),
        ('セキュリティ基礎','G. Mori','Security','脅威と対策', date(2019,2,2)),
        ('AI倫理','H. Sato','AI','AIと社会課題', date(2021,8,8)),
        ('UXデザイン','I. Ueda','Design','ユーザー中心設計', date(2018,4,18)),
        ('要件定義の技術','J. Oki','PM','合意形成の進め方', date(2017,2,14)),
        ('テスト入門','K. Abe','QA','テスト観点の基礎', date(2020,3,3)),
        ('経済学入門','L. Ono','Society','基礎経済学', date(2015,5,5)),
        ('統計学はじめの一歩','M. Wada','Math','やさしい統計', date(2016,8,23)),
        ('英作文のコツ','N. Hayashi','Language','書く力を鍛える', date(2014,12,12)),
        ('発声トレーニング','O. Arai','Music','声の出し方', date(2013,9,9)),
        ('登山の基本','P. Sugi','Hobby','安全な山歩き', date(2012,7,7)),
        ('写真術','Q. Hara','Hobby','構図と光', date(2011,3,21)),
        ('家庭菜園','R. Tani','Life','はじめての野菜作り', date(2010,10,1)),
        ('コーヒーの科学','S. Naka','Life','抽出の化学', date(2024,5,10)),
    ]
    Book.objects.bulk_create([Book(title=t,author=a,genre=g,summary=s,published_at=d) for t,a,g,s,d in data])
def unseed(apps, schema_editor):
    Book = apps.get_model('catalog','Book')
    Book.objects.all().delete()
class Migration(migrations.Migration):
    dependencies = [('catalog','0001_initial')]
    operations = [migrations.RunPython(seed, reverse_code=unseed)]
