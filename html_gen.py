
def create_html(filename, product_title, dis, price, prduct_main_image, product_sub_images, Video):
  html_str = """
  <!DOCTYPE html>
  <html>
  <head>
    <meta charset="utf-8">
    <title>KTG: Kristina Tech Gallery</title>
    <style type="text/css">
    body{
      margin: auto;
      margin-top: 20px;
    }
      .div1 {
        margin: 0px;
        padding: 0px;
        overflow: hidden;
        /*border: 1px solid blue;*/
        width: 1024px;
        margin: auto;
      }

      .div2 {
        margin: 12px;
        overflow: hidden;
        /*border: 1px solid blue;*/
        width: 100%;
        margin: auto;
      }

      img{
        width: 100%;
        height: 100%;
        display: block;
      }

      p{
        display: block;
        padding: 0px;
        margin-top: 0px;
      }
      h1{
        padding: 0px;
        margin-bottom: 0px;
      }
      #youtube_vd{
        width: 100%;
        height: 600px;
        background-color: #000;
        margin: auto;
        margin-top: 10px;
      }
      .divin{
        /*width: 30%;*/
        display: flex;
        /*justify-content: center;*/
        flex-direction: row;
        flex-wrap: wrap;
      }
      .divin0{
        /*width: 40%;*/
        width: 24vw;
        height: 24vw;
        min-width: 450px;
        min-height: 450px;
        margin: 5px;
      }
      .divin1{
        /*width: 40%;*/
        width: 11vw;
        height: 11vw;
        min-width: 30px;
        min-height: 30px;
        margin: 5px;
      }
      .divin2{
        /*width: 40%;*/
        width: 100%;
        /*height: 22vw;*/
        min-width: 270px;
        /*min-height: 270px;*/
        margin: 5px;
      }
    </style>
  </head>
  <body>
      <div class="div1">
        <a href="../index.html">Home</a>
        <div class="divin">
          <div class="divin0"><img src="https://ktg.aaja.co/pro_img/"""+prduct_main_image+""""/><p></p></div>
          <div class="divin2">
            <h1>"""+product_title+"""</h1>
            <p>"""+price+"""</p>
            <p>"""+dis+"""</p>
            <ul>
              <li>Mechanical Keyboard</li>
              <li>Blue switch</li>
              <li>Backlit Keys</li>
              <li>Light Mechanical Keyboard</li>
              <li>20 Running Light mode</li>
            </ul>
          </div>"""

  for product_sub_image in product_sub_images:
    html_str += '''<div class="divin1"><img src="https://ktg.aaja.co/pro_img/'''+product_sub_image+'''"/><p></p></div>'''
  
  html_str += '''
        </div>
      </div>'''
  if Video[0] != '':
    html_str += '''
        <div class="div1">
          <iframe id="youtube_vd" src="https://www.youtube.com/embed/'''+Video[0]+'''?rel=0&amp;autoplay=1&mute=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>'''
  html_str += '''<section>'''

  for product_sub_image in product_sub_images:
    html_str += '''<div class="div1"><img src="https://ktg.aaja.co/product_photo/jpg/KTGAB4.jpg"/><p>123</p></div>'''

  html_str += '''
    </section>
  </body>
  </html>
  '''

  # html_str += "<b>"+name+"</b>"

  Html_file= open("html/"+filename+".html","w")
  Html_file.write(html_str)
  Html_file.close()


product_title = "Track Mechanical Keyboard TK188"
dis = "N-TECH को नयाँ प्रस्तुती , उच्च गुणस्तरको Track TR 55 (AURA X ) <br/><br/>Sub Gaming mice अब नेपाली बजारमा उपलब्ध छ । 1600 DPI सम्मको resolution adjust गर्न मिल्ने यस माइस धेरै समय काम गर्दा तथा गेम खेल्दा हात नदुःख्ने प्रबिधि अर्थात (Ergonomically)डिज़ाइन गरीएको छ । Track Tr55 AuraX प्रयोग गरी अब ढुक्क संग घन्टौं काम गर्नुहोस्। N-TECH अब गुणस्तरमाँ No Compromise."
price = "Rs. 3800/-"
prduct_main_image = "jpg/KTGAA1.jpg"
product_sub_images = ['KTGAA1_2.jpg', 'KTGAA1_3.jpg']
product_image = ['jpg/KTGAB4.jpg', 'KTGAB4_1.jpg', 'KTGAB4_11A.JPG', 'KTGAB4_3.png']
yt_vid = "https://www.youtube.com/embed/XlCp2sHEyBg?rel=0&amp;autoplay=1&mute=1"
# create_html("filename", product_title, dis, price, prduct_main_image, product_sub_images)

import csv
with open('KTG_FB.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  line_count = 0
  for row in csv_reader:
    Code = row[1]
    Brand = row[2]
    Title = row[3]
    Description = row[4]
    Price = row[7]
    Image = row[9]
    Images = row[10].split("~")
    Video = row[11].split(",")
    print("--->", row[11].split(","), Video)
    create_html(Code, Title, Description, Price, Image, Images, Video)




    print(row[1], Image)
    print("---------")



