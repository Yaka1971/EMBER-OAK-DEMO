from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PAGE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>EMBER & OAK | Kitchen & Grill</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Montserrat:wght@500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{
  --black:#070605;--ink:#0d0907;--wood:#351006;--wood2:#571a0b;
  --gold:#dba844;--gold2:#f5cf79;--cream:#f3e7d2;--muted:#c7b6a4;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:#080605;color:var(--cream);font-family:Montserrat,Arial,sans-serif}
body:before{content:"";position:fixed;inset:0;pointer-events:none;z-index:-1;background:
 radial-gradient(circle at 18% 10%,rgba(117,35,12,.25),transparent 32%),
 linear-gradient(90deg,rgba(61,15,5,.25),transparent 25%,transparent 75%,rgba(61,15,5,.2))}
a{text-decoration:none;color:inherit}
.nav{height:72px;position:sticky;top:0;z-index:50;display:flex;align-items:center;justify-content:space-between;padding:0 5.5%;border-bottom:1px solid #7b351c;background:linear-gradient(90deg,#2b0b03f2,#120704f2,#2b0b03f2);backdrop-filter:blur(12px)}
.brand-mini{font-family:"Cormorant Garamond",serif;font-size:24px;font-weight:700;color:var(--gold2);letter-spacing:1px}
.links{display:flex;gap:30px;align-items:center;font-size:12px;letter-spacing:1.2px}
.links a{padding:26px 0 21px;border-bottom:2px solid transparent}
.links a:hover{color:var(--gold2);border-color:var(--gold)}
.reserve-small,.btn{border:1px solid var(--gold);color:var(--gold2);font-weight:800;letter-spacing:1.5px;text-transform:uppercase;border-radius:7px}
.reserve-small{padding:13px 20px;font-size:11px}
.menu-toggle{display:none;background:none;border:1px solid #a26e32;color:var(--gold2);padding:9px 12px;border-radius:6px;font-size:20px}

.hero{min-height:570px;display:grid;grid-template-columns:1.02fr .98fr;border-bottom:1px solid #7b351c;background:
 linear-gradient(90deg,#090503 0%,#110805 46%,transparent 67%),
 url("/images/hero-steak.jpg") right center/58% 100% no-repeat}
.hero-copy{display:flex;flex-direction:column;justify-content:center;padding:60px 4% 60px 8%}
.flame{font-size:62px;line-height:.8;color:var(--gold);filter:drop-shadow(0 0 12px #a65c1c)}
.logo-title{font-family:"Cormorant Garamond",serif;font-size:76px;line-height:.9;margin:15px 0 4px;color:var(--gold2);text-shadow:0 2px 0 #6c260d,0 0 22px #a75418;letter-spacing:-2px}
.logo-sub{display:inline-block;width:max-content;padding:6px 24px;border-top:1px solid var(--gold);border-bottom:1px solid var(--gold);font-family:"Cormorant Garamond",serif;font-size:25px;letter-spacing:5px;color:#fff}
.tagline{margin:20px 0 13px;color:var(--gold2);font-family:"Cormorant Garamond",serif;font-size:18px;letter-spacing:4px}
.hero-copy p{max-width:620px;font-family:"Cormorant Garamond",serif;font-size:24px;line-height:1.35;color:#eee;margin:0 0 25px}
.actions{display:flex;gap:16px;flex-wrap:wrap}
.btn{padding:16px 25px;font-size:12px;background:#0a0807}
.btn.gold{background:linear-gradient(#f5ce78,#d58d29);color:#150b05;border:none;box-shadow:0 8px 22px #0008}
.btn:hover{transform:translateY(-2px);filter:brightness(1.08)}
.hero-quote{display:flex;align-items:flex-start;justify-content:flex-end;padding:95px 7% 0 0;text-align:right}
.hero-quote .script{font-family:"Cormorant Garamond",serif;font-size:48px;font-style:italic;color:var(--gold2);line-height:.9;max-width:300px;text-shadow:0 2px 12px #000}
.hero-quote small{display:block;margin-top:14px;font-family:Montserrat;font-style:normal;font-size:11px;letter-spacing:4px}

.categories{padding:18px 6% 28px;background:linear-gradient(180deg,#120805,#090605)}
.category-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:20px}
.food-card{border:1px solid #b57925;border-radius:10px;overflow:hidden;background:#100a07;box-shadow:0 12px 30px #0008;transition:.25s}
.food-card:hover{transform:translateY(-5px);border-color:var(--gold2)}
.food-card img{width:100%;height:170px;object-fit:cover;display:block}
.food-card h3{text-align:center;font-family:"Cormorant Garamond",serif;color:var(--gold2);font-size:21px;letter-spacing:2px;margin:14px 8px 17px}

.story{display:grid;grid-template-columns:1.05fr 1fr .78fr;min-height:350px;border-top:1px solid #6b2a15;background:linear-gradient(90deg,#160906,#0c0806,#180b07)}
.story-photo img{width:100%;height:100%;object-fit:cover;display:block;filter:saturate(.9) contrast(1.06)}
.story-copy{padding:42px 38px}
.kicker{color:var(--gold);font-size:11px;letter-spacing:4px;font-weight:800;text-transform:uppercase}
.story h2,.menu-section h2,.experience h2{font-family:"Cormorant Garamond",serif;color:var(--gold2);font-size:42px;letter-spacing:2px;margin:5px 0 14px}
.story-copy p{font-family:"Cormorant Garamond",serif;font-size:20px;line-height:1.42;color:#eadfd2}
.reservation-box{align-self:center;margin:25px 25px 25px 0;padding:30px;border:1px solid #5b351d;border-radius:9px;background:#090806dd;box-shadow:0 18px 45px #0009}
.reservation-box h3{font-family:"Cormorant Garamond",serif;color:var(--gold2);font-size:27px;letter-spacing:2px;margin:0 0 15px}
.reservation-box p{color:var(--muted);font-family:"Cormorant Garamond",serif;font-size:19px;line-height:1.4}

.menu-section{padding:70px 7%;background:linear-gradient(#090605,#160a06)}
.section-head{text-align:center;max-width:750px;margin:0 auto 35px}
.section-head p{color:var(--muted);line-height:1.6}
.menu-list{max-width:1000px;margin:auto;display:grid;grid-template-columns:1fr 1fr;gap:16px 45px}
.menu-item{display:grid;grid-template-columns:1fr auto;gap:8px 20px;padding:18px 0;border-bottom:1px dotted #785330}
.menu-item h3{margin:0;font-family:"Cormorant Garamond",serif;font-size:24px;color:#fff}
.menu-item .price{color:var(--gold2);font-weight:800}
.menu-item p{grid-column:1/-1;margin:0;color:#a99786;font-size:13px;line-height:1.5}

.experience{padding:70px 7%;text-align:center;background:radial-gradient(circle at center,#321208,#090605 65%)}
.experience p{max-width:760px;margin:0 auto 28px;color:#d3c1b0;font-family:"Cormorant Garamond",serif;font-size:21px;line-height:1.5}
.hours{display:flex;justify-content:center;gap:55px;flex-wrap:wrap;margin:30px 0}
.hours div{min-width:180px}
.hours b{display:block;color:var(--gold2);font-family:"Cormorant Garamond",serif;font-size:22px}
.hours span{font-size:12px;color:#b8a28f;letter-spacing:1px}

footer{padding:28px 6%;display:flex;justify-content:space-between;gap:20px;align-items:center;border-top:1px solid #5f2815;background:#080503;color:#917f70;font-size:11px}
footer b{font-family:"Cormorant Garamond",serif;color:var(--gold2);font-size:22px}

@media(max-width:900px){
 .nav{height:auto;min-height:68px;flex-wrap:wrap;padding:14px 18px}.menu-toggle{display:block}.reserve-small{display:none}
 .links{display:none;width:100%;flex-direction:column;align-items:flex-start;gap:0;padding-top:12px}.links.open{display:flex}.links a{width:100%;padding:13px 0}
 .hero{grid-template-columns:1fr;min-height:760px;background:linear-gradient(180deg,#080402 0%,#0b0503e8 48%,#08040266 70%),url("/images/hero-steak.jpg") center bottom/cover no-repeat}
 .hero-copy{padding:65px 24px 20px;text-align:center;align-items:center}.logo-title{font-size:56px}.logo-sub{font-size:18px;letter-spacing:3px}.tagline{font-size:13px;letter-spacing:2px}.hero-copy p{font-size:21px}.actions{justify-content:center}
 .hero-quote{padding:20px 24px 60px;justify-content:center;text-align:center}.hero-quote .script{font-size:39px}
 .category-grid{grid-template-columns:1fr 1fr}.story{grid-template-columns:1fr}.story-photo{height:310px}.reservation-box{margin:0 22px 35px}.menu-list{grid-template-columns:1fr}
 footer{flex-direction:column;text-align:center}
}
@media(max-width:520px){
 .category-grid{grid-template-columns:1fr}.categories{padding:18px}.food-card img{height:210px}
 .logo-title{font-size:46px}.flame{font-size:48px}.hero-copy{padding-top:50px}
 .story-copy{padding:35px 24px}.story h2,.menu-section h2,.experience h2{font-size:35px}
}
</style>
</head>
<body>
<header class="nav">
  <a class="brand-mini" href="#home">EMBER & OAK</a>
  <button class="menu-toggle" onclick="document.querySelector('.links').classList.toggle('open')" aria-label="Menu">☰</button>
  <nav class="links">
    <a href="#home">HOME</a><a href="#menu">MENU</a><a href="#about">ABOUT</a>
    <a href="#reservations">RESERVATIONS</a><a href="#gallery">GALLERY</a><a href="#contact">CONTACT</a>
  </nav>
  <a class="reserve-small" href="/demo-reservation">RESERVE A TABLE</a>
</header>

<section class="hero" id="home">
 <div class="hero-copy">
   <div class="flame">♨</div>
   <h1 class="logo-title">EMBER <span>&</span> OAK</h1>
   <div class="logo-sub">KITCHEN & GRILL</div>
   <div class="tagline">GOOD FOOD • GREAT COMPANY • LASTING MEMORIES</div>
   <p>Bold flavors. Fresh ingredients. A dining experience that brings people together.</p>
   <div class="actions"><a class="btn gold" href="/demo-reservation">▣ &nbsp; RESERVE A TABLE</a><a class="btn" href="#menu">♜ &nbsp; VIEW OUR MENU</a></div>
 </div>
</section>

<section class="categories" id="gallery">
 <div class="category-grid">
  <article class="food-card"><img src="/images/seafood.jpg" alt="Fresh seafood"><h3>FRESH SEAFOOD</h3></article>
  <article class="food-card"><img src="/images/steak.jpg" alt="Premium steak"><h3>PREMIUM STEAKS</h3></article>
  <article class="food-card"><img src="/images/signature.jpg" alt="Signature pasta"><h3>SIGNATURE DISHES</h3></article>
  <article class="food-card"><img src="/images/dessert.jpg" alt="Dessert"><h3>DELICIOUS DESSERTS</h3></article>
 </div>
</section>

<section class="story" id="about">
 <div class="story-photo"><img src="/images/interior.jpg" alt="Ember and Oak dining room"></div>
 <div class="story-copy"><div class="kicker">THE EMBER & OAK EXPERIENCE</div><h2>OUR STORY</h2>
 <p>At Ember & Oak, we believe great food brings people together. Our menu is crafted with fresh, high-quality ingredients, inspired by flavor, culture, and community. Whether you're here for a casual meal or a special occasion, you're always family at our table.</p>
 <a class="btn" href="/our-story">LEARN MORE</a></div>
 <aside class="reservation-box" id="reservations"><div class="kicker">YOUR TABLE AWAITS</div><h3>MAKE A RESERVATION</h3>
 <p>Book your table and experience Ember & Oak in an intimate atmosphere built around unforgettable food.</p>
 <a class="btn gold" href="/demo-reservation">▣ &nbsp; RESERVE A TABLE</a></aside>
</section>

<section class="menu-section" id="menu">
 <div class="section-head"><div class="kicker">FROM OUR KITCHEN</div><h2>SIGNATURE MENU</h2><p>Wood-fired flavor, premium ingredients, and dishes designed to make the table the best part of your evening.</p></div>
 <div class="menu-list">
  <div class="menu-item"><h3>Oak-Fired Ribeye</h3><span class="price">$42</span><p>Prime ribeye, rosemary butter, roasted garlic, seasonal vegetables.</p></div>
  <div class="menu-item"><h3>Ember Salmon</h3><span class="price">$31</span><p>Char-grilled salmon, citrus herb glaze, asparagus, lemon.</p></div>
  <div class="menu-item"><h3>Blackened Shrimp Pasta</h3><span class="price">$28</span><p>Creole-spiced shrimp, creamy garlic sauce, parmesan, fresh herbs.</p></div>
  <div class="menu-item"><h3>Smoked Short Rib</h3><span class="price">$36</span><p>Slow-braised beef, cherry-wood jus, whipped potatoes, crispy shallots.</p></div>
  <div class="menu-item"><h3>Charred Garden Plate</h3><span class="price">$22</span><p>Fire-roasted seasonal vegetables, wild grains, herb vinaigrette.</p></div>
  <div class="menu-item"><h3>Molten Chocolate Ember</h3><span class="price">$13</span><p>Warm chocolate cake, vanilla cream, berries, dark chocolate glaze.</p></div>
 </div>
</section>

<section class="experience" id="contact">
 <div class="kicker">GOOD FOOD • GREAT COMPANY</div><h2>JOIN US AT THE TABLE</h2>
 <p>Come for the food. Stay for the atmosphere. Ember & Oak is designed for date nights, celebrations, family dinners, and evenings worth remembering.</p>
 <div class="hours"><div><b>MON–THU</b><span>4:00 PM – 10:00 PM</span></div><div><b>FRI–SAT</b><span>4:00 PM – 11:00 PM</span></div><div><b>SUNDAY</b><span>3:00 PM – 9:00 PM</span></div></div>
 <div class="actions" style="justify-content:center"><a class="btn gold" href="/demo-reservation">RESERVE A TABLE</a><a class="btn" href="/demo-contact">CONTACT US</a></div>
</section>

<footer><b>EMBER & OAK</b><span>Kitchen & Grill • Demo Restaurant Experience</span><span>Powered by MAYAKA'AL DIGITAL.</span></footer>
<script>
document.querySelectorAll('.links a').forEach(a=>a.addEventListener('click',()=>document.querySelector('.links').classList.remove('open')));
</script>
</body></html>"""

@app.route("/")
def home():
    return render_template_string(PAGE)


DETAIL_PAGE = r"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{{ title }} | EMBER & OAK</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Montserrat:wght@500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{--gold:#dba844;--gold2:#f5cf79;--cream:#f3e7d2;--muted:#c7b6a4}
*{box-sizing:border-box}body{margin:0;background:#080605;color:var(--cream);font-family:Montserrat,Arial,sans-serif}a{text-decoration:none;color:inherit}
.top{min-height:72px;display:flex;align-items:center;justify-content:space-between;padding:0 6%;border-bottom:1px solid #7b351c;background:linear-gradient(90deg,#2b0b03,#120704,#2b0b03)}
.brand{font-family:"Cormorant Garamond",serif;font-size:26px;font-weight:700;color:var(--gold2)}
.back{border:1px solid var(--gold);padding:12px 17px;border-radius:7px;color:var(--gold2);font-size:11px;font-weight:800;letter-spacing:1px}
.wrap{min-height:calc(100vh - 72px);display:grid;place-items:center;padding:60px 22px;background:radial-gradient(circle at 50% 25%,#351208,#080605 62%)}
.card{width:min(900px,100%);padding:clamp(30px,6vw,65px);border:1px solid #8c5428;border-radius:12px;background:linear-gradient(145deg,#130a07,#090605);box-shadow:0 25px 70px #000a}
.kicker{color:var(--gold);font-size:11px;letter-spacing:4px;font-weight:800;text-transform:uppercase}
h1{font-family:"Cormorant Garamond",serif;font-size:clamp(45px,8vw,78px);line-height:.95;color:var(--gold2);margin:10px 0 24px}
p{font-family:"Cormorant Garamond",serif;font-size:21px;line-height:1.62;color:#e7d9ca}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:30px}.block{padding:24px;border-top:1px solid #70401f;background:#0d0806}
.block h2{font-family:"Cormorant Garamond",serif;color:var(--gold2);margin:0 0 8px;font-size:28px}.block p{font-size:18px;margin:0;color:var(--muted)}
.note{margin-top:28px;padding:22px;border-left:3px solid var(--gold);background:#160c07}.note b{display:block;color:var(--gold2);margin-bottom:8px}.note p{font-size:18px;margin:0}
.action{display:inline-block;margin-top:25px;padding:15px 22px;border-radius:7px;background:linear-gradient(#f5ce78,#d58d29);color:#150b05;font-size:12px;font-weight:900;letter-spacing:1.2px}
footer{text-align:center;padding:25px;color:#917f70;font-size:11px;border-top:1px solid #5f2815}
@media(max-width:700px){.grid{grid-template-columns:1fr}.top{padding:0 18px}.brand{font-size:21px}.card{padding:30px 22px}p{font-size:19px}}
</style></head><body>
<header class="top"><a class="brand" href="/">EMBER & OAK</a><a class="back" href="/">BACK TO SITE</a></header>
<main class="wrap"><section class="card"><div class="kicker">{{ kicker }}</div><h1>{{ title }}</h1>{{ body|safe }}<a class="action" href="/">RETURN TO EMBER & OAK</a></section></main>
<footer>EMBER & OAK • Demo Restaurant Experience • Powered by MAYAKA'AL DIGITAL.</footer>
</body></html>"""

@app.route("/our-story")
def our_story():
    body = """
<p>Ember & Oak was imagined around a simple idea: the best meals are not rushed. They are shared. The experience brings together the warmth of an open flame, the character of wood-fired cooking, and a dining room designed for conversation, celebration, and connection.</p>
<p>The kitchen centers its identity on bold, familiar flavors elevated through careful preparation. Premium steaks, fresh seafood, signature dishes, seasonal ingredients, and rich desserts give the menu a balance between comfort and occasion.</p>
<div class="grid">
<div class="block"><h2>Fire & Flavor</h2><p>Wood-fired techniques and char-grilled finishes form the heart of the Ember & Oak culinary identity.</p></div>
<div class="block"><h2>Gather Together</h2><p>The atmosphere is designed for date nights, family dinners, celebrations, and evenings worth remembering.</p></div>
<div class="block"><h2>Quality First</h2><p>The concept emphasizes fresh ingredients, thoughtful preparation, and dishes presented with care.</p></div>
<div class="block"><h2>Warm Hospitality</h2><p>From the first welcome to the final course, the experience is built around making guests feel at home.</p></div>
</div>
<div class="note"><b>PORTFOLIO DEMONSTRATION</b><p>Ember & Oak is a MAYAKA'AL DIGITAL demonstration brand. For a real restaurant client, this story would be replaced with the restaurant's authentic history, founders, culinary philosophy, team, and brand story.</p></div>
"""
    return render_template_string(DETAIL_PAGE, kicker="THE EMBER & OAK EXPERIENCE", title="OUR STORY", body=body)

@app.route("/demo-reservation")
def demo_reservation():
    body = """
<p>This page demonstrates the reservation experience for the Ember & Oak portfolio website. Because Ember & Oak is a demonstration brand, no real table is booked and no fictional reservation information is collected.</p>
<div class="grid">
<div class="block"><h2>Live Client Version</h2><p>This action can connect visitors to the restaurant's real reservation platform, booking form, telephone system, or supported third-party reservation service.</p></div>
<div class="block"><h2>Customer Journey</h2><p>A real guest would select or request a date, time, party size, and supported reservation details through the client's chosen system.</p></div>
</div>
<div class="note"><b>DEMO MODE</b><p>This demonstration shows how the feature fits into the website without pretending that a reservation has been made with a fictional restaurant.</p></div>
"""
    return render_template_string(DETAIL_PAGE, kicker="YOUR TABLE AWAITS", title="RESERVATION DEMO", body=body)

@app.route("/demo-contact")
def demo_contact():
    body = """
<p>This page demonstrates where a real restaurant website would handle guest questions, event inquiries, private dining requests, feedback, and other customer messages.</p>
<div class="grid">
<div class="block"><h2>Real Contact Details</h2><p>A live client website would use the restaurant's verified email address, telephone number, location, and preferred customer-contact channels.</p></div>
<div class="block"><h2>Contact Form</h2><p>The site can also be connected to a working inquiry form that routes messages to the client's real business inbox.</p></div>
</div>
<div class="note"><b>DEMO MODE</b><p>No fake email address or fictional contact information is presented as though it belongs to a real operating restaurant.</p></div>
"""
    return render_template_string(DETAIL_PAGE, kicker="GET IN TOUCH", title="CONTACT DEMO", body=body)

@app.route("/images/<path:filename>")
def images(filename):
    return send_from_directory(os.path.join(BASE_DIR, "images"), filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")), debug=True)
