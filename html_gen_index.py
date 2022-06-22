
def create_html(products):
  html_str = """<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <meta charset="utf-8">
  <title>KTG: Kristina Tech Gallery</title>
  <style type="text/css">

    section {
      /*width: 200px;*/
      /*border: 2px solid red;*/
      display: flex;
      justify-content: center;
      flex-direction: row;
      /*align-items: center;*/
      margin: auto;
      /*height: calc(100vh - 16px);*/
      /*min-width: 600px;*/
      flex-wrap: wrap;
      max-width: 1320px;
    }

    div {
      /*color: #fff;*/
      /*background: #2d2d2d;*/
      margin: 12px;
      /*display: inline-block;*/
      /*width: 30%;*/
      overflow: hidden;
      /*border: 1px solid blue;*/
      width: 22vw;
      height: 22vw;
      min-width: 300px;
      min-height: 300px;

    }

    img{
      width: 100%;
      height: 100%;
      display: block;
    }

    p{
      border: 1px solid yellow;
  /*position: absolute;*/
  /*bottom: 8px;*/
  /*left: 16px;*/
    }
    @media only screen and (max-width: 900px) {
  body {
    background-color: lightblue;
  }

    div {
      /*color: #fff;*/
      /*background: #2d2d2d;*/
      /*margin: 12px;*/
      /*display: inline-block;*/
      /*width: 30%;*/
      overflow: hidden;
      /*border: 1px solid blue;*/
      width: 22vw;
      height: 22vw;
      min-width: 120px;
      min-height: 120px;
      margin: 5px;
      padding: 0px;

    }
}
  </style>
</head>
<body>
  <section>"""

  for product in products:
    html_str += '''<a href="html/'''+product+'''.html"><div><img src="https://ktg.aaja.co/product_photo/jpg/'''+product+'''.jpg"/><p>123</p></div></a>'''
  
  html_str += '''
        </section>
</body>
</html>
  '''

  # html_str += "<b>"+name+"</b>"

  Html_file= open("index.html","w")
  Html_file.write(html_str)
  Html_file.close()

import csv
products = []
with open('KTG_FB.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  line_count = 0
  for row in csv_reader:
    if line_count != 0:
      products.append(row[1])

    line_count += 1

create_html(products)

