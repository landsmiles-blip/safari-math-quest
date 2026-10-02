# -*- coding: utf-8 -*-
"""
MEP Primary 3 Safari Science Quest Generator
Visual Makeover: Geeky Einstein Quantum Science Laboratory
Features:
- Futuristic Einstein Quantum Research Lab atmosphere
- Big glowing glass condenser tubes with bubbling neon liquids
- Vibranium nuclear fusion containment core & dark matter plasma ring
- Neon holographic equations: E=mc², F=ma, ΔQ=mcΔT, Fg=G*m1*m2/r², C6H12O6+6O2➔6CO2+6H2O, ∇·B=0
- Professor Pip the Lion Cub with wild Einstein hair, glowing spectacles, lab coat, and bubbling flask
- Corrected ramp illustration: Down from high left to floor right; rough towel flat ON THE FLOOR AT BOTTOM
- Exam Mode life cycle questions: No stage names (Stage 1 ➔ Stage 2 ➔ Stage 3 ➔ Stage 4)
- Much bigger, richer illustrations: Large cow eating grass, big lion with steak, bread & rice, 3D magnets, copper chocolate pan
- 100% preservation of all 5 Discovery Labs, 15 exam questions, scoring, sound synthesizer, and certificate logic
"""
import os

def get_html_content():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
<title>🔬 Safari Science Quest · Professor Pip's Einstein Quantum Lab</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fredoka+One&family=Nunito:wght@700;800;900&family=JetBrains+Mono:wght@700;800&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;-webkit-tap-highlight-color:transparent}
:root{
  --fd:'Fredoka One',cursive;
  --fb:'Nunito',sans-serif;
  --fm:'JetBrains Mono',monospace;
  --gold:#ffd166;
  --gold-glow:rgba(255,209,102,0.85);
  --cyan:#00f5d4;
  --cyan-glow:rgba(0,245,212,0.65);
  --blue:#00b4d8;
  --neon-lime:#10b981;
  --neon-purple:#a855f7;
  --deep-bg:#060919;
  --r:clamp(14px,3vw,24px);
}
html,body{width:100%;height:100%;overflow:hidden;font-family:var(--fb);background:var(--deep-bg);color:#fff}

/* ── SCI-FI QUANTUM RESEARCH LABORATORY BACKDROP ── */
#bg{position:fixed;inset:0;z-index:0;
  background:radial-gradient(ellipse at 50% 15%, #0d1b3e 0%, #060919 55%, #02040a 100%);
  overflow:hidden}

/* Cybernetic Grid Floor & Ceiling */
.cyber-grid{position:absolute;inset:0;pointer-events:none;
  background-image:linear-gradient(rgba(0,245,212,0.06) 1px, transparent 1px),
                   linear-gradient(90deg, rgba(0,245,212,0.06) 1px, transparent 1px);
  background-size:48px 48px;
  mask-image:radial-gradient(circle at 50% 40%, rgba(0,0,0,0.85) 20%, rgba(0,0,0,0.1) 80%);
  -webkit-mask-image:radial-gradient(circle at 50% 40%, rgba(0,0,0,0.85) 20%, rgba(0,0,0,0.1) 80%)}

/* Vibranium Fusion Containment Ring (Center-Top Core) */
.fusion-core-wrap{position:absolute;top:-40px;left:50%;transform:translateX(-50%);
  width:clamp(280px,50vw,460px);height:clamp(280px,50vw,460px);
  pointer-events:none;z-index:1;opacity:0.85}
.fusion-svg{width:100%;height:100%;display:block;animation:corePulse 6s infinite ease-in-out alternate}
@keyframes corePulse{
  0%{transform:scale(0.97);filter:drop-shadow(0 0 25px rgba(0,245,212,0.45))}
  50%{transform:scale(1.03);filter:drop-shadow(0 0 45px rgba(168,85,247,0.65))}
  100%{transform:scale(0.97);filter:drop-shadow(0 0 25px rgba(0,245,212,0.45))}
}
.rot-ring-cw{transform-origin:center;animation:spinCw 24s linear infinite}
.rot-ring-ccw{transform-origin:center;animation:spinCcw 18s linear infinite}
@keyframes spinCw{from{transform:rotate(0deg)}to{transform:rotate(360deg)}}
@keyframes spinCcw{from{transform:rotate(360deg)}to{transform:rotate(0deg)}}

/* Big Glowing Glass Condenser Tubes (Left & Right Flanks) */
.condenser-tube{position:absolute;top:0;bottom:0;width:clamp(42px,6vw,68px);pointer-events:none;z-index:2;display:flex;flex-direction:column;align-items:center}
.condenser-tube.left{left:clamp(6px,1.5vw,22px)}
.condenser-tube.right{right:clamp(6px,1.5vw,22px)}
.tube-glass{width:100%;height:100%;position:relative;border-radius:30px;
  background:linear-gradient(90deg, rgba(255,255,255,0.15) 0%, rgba(255,255,255,0.03) 40%, rgba(0,245,212,0.08) 70%, rgba(255,255,255,0.2) 100%);
  border:2px solid rgba(0,245,212,0.35);box-shadow:inset 0 0 16px rgba(0,245,212,0.25),0 0 24px rgba(0,245,212,0.2);
  overflow:hidden}
.condenser-tube.right .tube-glass{
  border-color:rgba(168,85,247,0.35);box-shadow:inset 0 0 16px rgba(168,85,247,0.25),0 0 24px rgba(168,85,247,0.2);
  background:linear-gradient(90deg, rgba(255,255,255,0.15) 0%, rgba(255,255,255,0.03) 40%, rgba(168,85,247,0.08) 70%, rgba(255,255,255,0.2) 100%)}
.tube-liquid{position:absolute;bottom:0;left:0;right:0;height:70%;
  background:linear-gradient(180deg, rgba(0,245,212,0.7) 0%, rgba(16,185,129,0.85) 100%);
  box-shadow:0 0 30px rgba(0,245,212,0.6);animation:liquidWave 4s infinite ease-in-out alternate}
.condenser-tube.right .tube-liquid{
  height:65%;
  background:linear-gradient(180deg, rgba(168,85,247,0.75) 0%, rgba(236,72,153,0.85) 100%);
  box-shadow:0 0 30px rgba(168,85,247,0.6);animation:liquidWave2 4.5s infinite ease-in-out alternate}
@keyframes liquidWave{0%{height:68%;opacity:0.85}100%{height:74%;opacity:0.95}}
@keyframes liquidWave2{0%{height:63%;opacity:0.85}100%{height:70%;opacity:0.95}}

/* Coiled Condenser Spiral inside Glass */
.spiral-svg{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;opacity:0.4}

/* Rising Bubbles inside Tubes */
.tube-bubble{position:absolute;background:rgba(255,255,255,0.85);border-radius:50%;
  box-shadow:0 0 8px #fff;animation:riseBubble var(--dur,4s) var(--del,0s) infinite linear}
@keyframes riseBubble{
  0%{bottom:0%;transform:translateX(0) scale(0.6);opacity:0}
  20%{opacity:0.85}
  80%{opacity:0.85}
  100%{bottom:72%;transform:translateX(var(--drift,6px)) scale(1.2);opacity:0}
}

/* Holographic Floating Chalkboard Equations */
.holo-eq{position:absolute;font-family:var(--fm);font-size:clamp(.8rem,1.9vw,1.05rem);
  font-weight:800;pointer-events:none;z-index:2;user-select:none;
  padding:3px 10px;border-radius:6px;background:rgba(6,15,35,0.45);
  border:1px solid rgba(0,245,212,0.3);
  color:rgba(0,245,212,0.85);text-shadow:0 0 10px rgba(0,245,212,0.75);
  animation:floatHolo var(--d,6s) var(--del,0s) infinite ease-in-out alternate}
.holo-eq.purple{color:rgba(192,132,252,0.9);border-color:rgba(168,85,247,0.4);text-shadow:0 0 10px rgba(168,85,247,0.75)}
.holo-eq.gold{color:rgba(255,209,102,0.9);border-color:rgba(255,209,102,0.4);text-shadow:0 0 10px rgba(255,209,102,0.75)}
.holo-eq.lime{color:rgba(52,211,153,0.9);border-color:rgba(16,185,129,0.4);text-shadow:0 0 10px rgba(16,185,129,0.75)}
@keyframes floatHolo{
  0%{transform:translateY(0) scale(1);opacity:0.75}
  50%{transform:translateY(-8px) scale(1.03);opacity:0.95}
  100%{transform:translateY(4px) scale(0.98);opacity:0.7}
}

/* Floating Science Bubbles */
.sci-bubble{position:absolute;border-radius:50%;pointer-events:none;z-index:2;
  background:radial-gradient(circle at 35% 35%,rgba(255,255,255,0.85),rgba(0,245,212,0.3) 60%,rgba(168,85,247,0.4) 100%);
  border:1.5px solid rgba(255,255,255,0.75);
  box-shadow:0 0 16px rgba(0,245,212,0.55);
  animation:floatBubble var(--dur,6s) var(--del,0s) infinite ease-in-out alternate}
@keyframes floatBubble{
  0%{transform:translate(0,0) scale(0.9);opacity:0.4}
  50%{transform:translate(14px,-24px) scale(1.15);opacity:0.9}
  100%{transform:translate(-10px,-48px) scale(0.95);opacity:0.35}
}

/* Glowing Stars */
.star{position:absolute;background:#ffd166;border-radius:50%;pointer-events:none;z-index:1;
  animation:twk var(--d,3s) var(--dl,0s) infinite alternate ease-in-out}
@keyframes twk{0%{opacity:.25;transform:scale(.7)}100%{opacity:1;transform:scale(1.4)}}

/* Lab Ground Platform with Laser Guide Lines */
.ground{position:absolute;bottom:0;left:0;right:0;height:12%;
  background:linear-gradient(180deg,#0a192f 0%,#050c18 60%,#02040a 100%);
  border-top:2px solid rgba(0,245,212,0.5);
  box-shadow:0 -6px 24px rgba(0,245,212,0.25);
  z-index:2;pointer-events:none}
.ground::after{content:'';position:absolute;top:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,rgba(0,245,212,0.8),transparent)}

/* ── NAME MODAL ── */
#name-modal{position:fixed;inset:0;z-index:3000;display:flex;align-items:center;justify-content:center;
  background:rgba(4,9,24,.92);backdrop-filter:blur(22px);padding:16px}
#name-modal.hide{display:none}
.nm-card{background:linear-gradient(135deg,rgba(10,25,55,.96),rgba(8,38,58,.94));
  border:2.5px solid rgba(0,245,212,.75);border-radius:var(--r);padding:clamp(22px,4vw,38px);
  text-align:center;width:100%;max-width:460px;
  box-shadow:0 24px 64px rgba(0,0,0,.7),0 0 60px rgba(0,245,212,.35)}
.nm-pip-avatar{width:110px;height:110px;margin:0 auto 12px;filter:drop-shadow(0 0 20px rgba(0,245,212,.6));animation:bob 3s infinite ease-in-out alternate}
.nm-card h2{font-family:var(--fd);color:var(--gold);font-size:clamp(1.4rem,5vw,2rem);margin-bottom:6px;text-shadow:0 0 20px rgba(255,209,102,.6)}
.nm-card p{color:rgba(255,255,255,.9);font-size:clamp(.85rem,2.5vw,1rem);font-weight:700;margin-bottom:18px}
#nm-input{width:100%;padding:clamp(12px,3vw,16px) 20px;border-radius:100px;
  border:3px solid rgba(0,245,212,.7);background:rgba(255,255,255,.14);
  color:#fff;font-family:var(--fd);font-size:clamp(1.1rem,4vw,1.45rem);text-align:center;
  outline:none;transition:border-color .2s;margin-bottom:16px}
#nm-input::placeholder{color:rgba(255,255,255,.5);font-family:var(--fb)}
#nm-input:focus{border-color:var(--gold);box-shadow:0 0 18px rgba(255,209,102,.7)}

/* ── BUTTONS ── */
.btn{font-family:var(--fd);letter-spacing:.3px;border:none;border-radius:100px;
  cursor:pointer;position:relative;top:0;
  transition:top .1s,box-shadow .1s,filter .1s,transform .1s;
  text-shadow:0 2px 4px rgba(0,0,0,.35);font-size:clamp(.92rem,2.8vw,1.15rem);
  padding:clamp(10px,2.2vw,14px) clamp(16px,4vw,26px);color:#fff;display:inline-flex;align-items:center;justify-content:center;gap:6px;z-index:20}
.btn:active{top:4px;filter:brightness(.92)}
.btn.full{width:100%;display:flex}
.bg{background:#10b981;box-shadow:0 5px 0 #047857,0 8px 18px rgba(16,185,129,.4)}
.by{background:#ffd166;box-shadow:0 5px 0 #f48c06,0 8px 18px rgba(255,209,102,.4);color:#78350f}
.bb{background:#00b4d8;box-shadow:0 5px 0 #0077b6,0 8px 18px rgba(0,180,216,.4);color:#fff}
.bpk{background:#ff70a6;box-shadow:0 5px 0 #c9184a,0 8px 18px rgba(255,112,166,.4)}
.bpu{background:#8b5cf6;box-shadow:0 5px 0 #6d28d9,0 8px 18px rgba(139,92,246,.4)}
.bo{background:#ff9f1c;box-shadow:0 5px 0 #e85d04,0 8px 18px rgba(255,159,28,.4)}
.btn-gold{background:linear-gradient(135deg,#ffd166,#ff9f1c);box-shadow:0 5px 0 #d97706,0 0 0 0 rgba(255,209,102,.6);
  color:#78350f;animation:gp 1.4s infinite;font-size:clamp(.95rem,3.2vw,1.25rem)}
@keyframes gp{0%,100%{box-shadow:0 5px 0 #d97706,0 0 0 0 rgba(255,209,102,.6)}50%{box-shadow:0 5px 0 #d97706,0 0 0 14px rgba(255,209,102,0)}}

/* ── APP SHELL ── */
#app{position:relative;z-index:10;width:100%;height:100%;
  display:flex;flex-direction:column;align-items:center;
  padding:clamp(4px,1vw,8px);gap:clamp(4px,1vw,8px);overflow:hidden}

/* ── TOPBAR ── */
#topbar{width:100%;max-width:920px;display:flex;align-items:center;justify-content:space-between;
  padding:6px 16px;background:rgba(6,18,42,.88);backdrop-filter:blur(20px);
  border-radius:100px;border:1.8px solid rgba(0,245,212,.5);box-shadow:0 0 20px rgba(0,245,212,0.25);
  flex-shrink:0;z-index:25}
.brand{display:flex;align-items:center;gap:10px}
.brand .pip-badge{width:38px;height:38px;display:flex;align-items:center;justify-content:center;
  border-radius:50%;background:rgba(0,245,212,0.2);border:1.5px solid var(--cyan);
  box-shadow:0 0 12px rgba(0,245,212,0.5)}
.brand h1{font-family:var(--fd);color:var(--gold);font-size:clamp(.95rem,3vw,1.3rem);
  text-shadow:0 0 14px rgba(255,209,102,.6)}
.topright{display:flex;align-items:center;gap:8px}
.stamp{background:linear-gradient(135deg,#10b981,#047857);border-radius:100px;
  padding:4px 12px;font-size:.76rem;font-weight:900;color:#fff;
  box-shadow:0 2px 8px rgba(16,185,129,.4);display:none}
.stamp.on{display:flex;align-items:center;gap:4px}
.ppill{display:flex;align-items:center;gap:6px;background:rgba(255,255,255,.16);
  border:1.5px solid rgba(255,255,255,.3);border-radius:100px;padding:4px 12px 4px 8px;
  cursor:pointer;color:#fff;font-family:var(--fb);font-weight:800;font-size:.85rem;
  transition:background .2s,transform .15s}
.ppill:hover{background:rgba(255,255,255,.26);transform:scale(1.03)}
.ppill .pnm{color:var(--gold);max-width:110px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}

/* ── MAIN ── */
#main{width:100%;max-width:920px;flex:1;min-height:0;display:flex;flex-direction:column;position:relative;z-index:15}
.screen{display:none;flex-direction:column;height:100%}
.screen.active{display:flex}

/* ── CARD STYLES ── */
.glass{background:rgba(255,255,255,.12);backdrop-filter:blur(18px);
  border:1.5px solid rgba(255,255,255,.28);border-radius:var(--r);
  box-shadow:0 8px 32px rgba(0,0,0,.35),inset 0 1px 0 rgba(255,255,255,.2)}
.card{background:rgba(8,26,56,.9);backdrop-filter:blur(22px);
  border:1.8px solid rgba(0,245,212,.5);border-radius:var(--r);
  box-shadow:0 12px 36px rgba(0,0,0,.45),inset 0 1px 0 rgba(255,255,255,.18)}

/* ── SCREEN: START ── */
#sc-start{flex:1;align-items:center;justify-content:center;gap:clamp(10px,2vw,18px)}
.hero{text-align:center;color:#fff;display:flex;flex-direction:column;align-items:center}
.hero-pip-wrap{width:clamp(110px,18vw,145px);height:clamp(110px,18vw,145px);margin-bottom:4px;
  filter:drop-shadow(0 0 28px rgba(0,245,212,0.7));animation:bob 3s infinite ease-in-out alternate}
@keyframes bob{0%{transform:translateY(0)}100%{transform:translateY(-10px)}}
.hero h2{font-family:var(--fd);font-size:clamp(1.6rem,5.5vw,2.8rem);color:var(--gold);
  text-shadow:0 0 32px rgba(255,209,102,.95),0 3px 0 rgba(0,0,0,.35);line-height:1.15;letter-spacing:.5px}
.hero p{font-size:clamp(.88rem,2.4vw,1.15rem);color:rgba(255,255,255,.92);margin-top:4px;font-weight:800;text-shadow:0 2px 8px rgba(0,0,0,.3)}
.mode-grid{width:100%;max-width:820px;display:grid;grid-template-columns:1fr 1fr;gap:clamp(12px,2.6vw,22px)}
.mcard{padding:clamp(16px,2.8vw,26px);display:flex;flex-direction:column;align-items:center;text-align:center;gap:8px;border-radius:clamp(16px,3vw,26px)}
.mcard .mi{font-size:clamp(2.2rem,5.2vw,3.2rem);filter:drop-shadow(0 4px 8px rgba(0,0,0,.25))}
.mcard .mt{font-family:var(--fd);color:var(--gold);font-size:clamp(1.08rem,3vw,1.38rem);letter-spacing:.4px}
.mcard .md{color:rgba(255,255,255,.86);font-size:clamp(.78rem,2vw,.96rem);font-weight:700;line-height:1.35}
.mcard .ml{font-size:clamp(.72rem,1.8vw,.84rem);color:rgba(255,255,255,.65);font-weight:800;margin-top:2px}

/* ── SCREEN: TRAINING / DISCOVERY LABS ── */
#sc-train{flex:1;gap:clamp(8px,2vw,12px)}
.tbar{display:flex;align-items:center;gap:10px;flex-shrink:0;
  background:rgba(6,20,44,.85);backdrop-filter:blur(16px);
  border-radius:100px;border:1.8px solid rgba(0,245,212,.48);
  padding:5px 14px;width:100%}
.bk{background:rgba(255,255,255,.16);border:1.5px solid rgba(255,255,255,.3);
  border-radius:100px;padding:5px 14px;color:#fff;font-weight:800;font-size:.85rem;
  cursor:pointer;transition:background .2s;z-index:20}
.bk:hover{background:rgba(255,255,255,.28)}
.tbar-title{font-family:var(--fd);color:var(--gold);font-size:clamp(.9rem,2.6vw,1.18rem);
  text-shadow:0 0 10px rgba(255,209,102,.5)}
.camps{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));
  gap:clamp(8px,2vw,14px);flex:1;min-height:0;align-content:start}
.camp{display:flex;flex-direction:column;align-items:center;justify-content:center;
  text-align:center;gap:6px;padding:clamp(12px,2.5vw,20px);cursor:pointer;
  transition:transform .2s,box-shadow .2s;border-radius:20px}
.camp:hover{transform:translateY(-4px);box-shadow:0 12px 28px rgba(0,245,212,.35)}
.camp:active{transform:scale(.97)}
.camp .ci{font-size:clamp(1.8rem,4.5vw,2.5rem);filter:drop-shadow(0 2px 6px rgba(0,0,0,.3))}
.camp .cn{font-family:var(--fd);color:var(--gold);font-size:clamp(.84rem,2.3vw,1.02rem)}
.camp .cd{color:rgba(255,255,255,.75);font-size:clamp(.68rem,1.8vw,.82rem);font-weight:700}
.camp .cs{font-size:1.15rem;margin-top:2px}

/* Training Practice Area */
#t-prac{flex:1;min-height:0;display:none;flex-direction:column;gap:clamp(8px,2vw,12px)}
#t-prac.visible{display:flex}

/* ── DUAL-CARD REDESIGNED SCIENCE DISPLAY ── */
#lab-card, #qcard{padding:clamp(10px,2vw,16px);display:flex;flex-direction:column;
  align-items:center;justify-content:flex-start;text-align:center;
  gap:clamp(6px,1.2vw,9px);flex:1;min-height:0;position:relative;z-index:15}
.lab-badge, .zbadge{font-family:var(--fd);font-size:clamp(.72rem,1.8vw,.86rem);
  padding:3px 14px;border-radius:100px;background:rgba(0,245,212,.18);
  border:1px solid rgba(0,245,212,.5);color:var(--cyan);letter-spacing:.5px;flex-shrink:0}
#lab-prompt, #q-prompt{font-size:clamp(.92rem,2.5vw,1.18rem);color:#fff;
  font-weight:800;flex-shrink:0;max-width:100%}

/* The Main Visual Spotlight Box (Generously Sized, Rich Illustrations) */
#lab-disp, #q-disp{width:100%;background:rgba(4,14,35,.62);border:1.8px solid rgba(0,245,212,.4);
  border-radius:clamp(14px,2.5vw,20px);
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  padding:clamp(8px,1.5vw,14px);
  overflow:visible;text-align:center;flex:1;
  min-height:clamp(135px,24vh,195px);max-height:clamp(165px,30vh,230px);position:relative}

/* Inner graphic spotlight container */
.disp-spotlight{display:flex;align-items:center;justify-content:center;width:100%;flex:1}
.disp-spotlight svg{width:100%;max-width:480px;height:auto;max-height:140px;display:block}

/* Concept label pill (generously spaced beneath graphics, never squished) */
.disp-pill{margin-top:6px;font-family:var(--fd);font-size:clamp(.74rem,1.9vw,.92rem);
  letter-spacing:.4px;padding:3px 14px;border-radius:100px;background:rgba(0,0,0,.5);
  border:1.5px solid rgba(0,245,212,.5);color:var(--gold);text-shadow:0 0 10px rgba(255,209,102,.6);flex-shrink:0}

/* Choices Row */
.lab-choices{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;width:100%;flex-shrink:0;z-index:20}
.lab-choice-btn{font-family:var(--fd);font-size:clamp(.88rem,2.4vw,1.08rem);
  padding:clamp(10px,2.2vw,14px) clamp(16px,3.5vw,24px);border-radius:100px;border:none;cursor:pointer;
  color:#fff;background:linear-gradient(135deg,#0284c7,#0369a1);
  box-shadow:0 4px 0 #075985,0 6px 16px rgba(2,132,199,.35);
  transition:transform .12s,filter .12s;display:inline-flex;align-items:center;gap:8px;z-index:20}
.lab-choice-btn:hover{filter:brightness(1.1);transform:scale(1.02)}
.lab-choice-btn:active{transform:scale(.97)}

/* Discovery Success Banner */
.lab-success-banner{background:linear-gradient(135deg,rgba(16,185,129,.94),rgba(5,150,105,.96));
  border:2px solid #34d399;border-radius:16px;padding:clamp(8px,1.8vw,12px) 16px;
  width:100%;display:none;align-items:center;justify-content:space-between;gap:10px;
  box-shadow:0 6px 20px rgba(16,185,129,.35);animation:fadeIn .3s;z-index:20}
@keyframes fadeIn{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:translateY(0)}}
.lab-success-txt{font-size:clamp(.82rem,2.2vw,.98rem);font-weight:800;color:#fff;text-align:left;line-height:1.35}

/* ── SCREEN: EXAM ── */
#sc-exam{gap:clamp(7px,1.8vw,12px);flex:1}
.prow{display:flex;align-items:center;gap:10px;flex-shrink:0;
  background:rgba(6,20,44,.85);backdrop-filter:blur(16px);
  border-radius:100px;border:1.8px solid rgba(0,245,212,.48);
  padding:5px 14px;width:100%}
.qlbl{font-family:var(--fd);color:var(--gold);font-size:clamp(.84rem,2.3vw,1.08rem);
  white-space:nowrap;text-shadow:0 0 12px rgba(255,209,102,.7)}
.ptrack{flex:1;height:clamp(9px,1.8vw,14px);background:rgba(0,0,0,.38);border-radius:100px;
  overflow:hidden;border:1.5px solid rgba(255,255,255,.18)}
.pfill{height:100%;background:linear-gradient(90deg,#00f5d4,#00b4d8);border-radius:100px;
  transition:width .4s ease;box-shadow:0 0 10px rgba(0,245,212,.7)}
.slbl{font-family:var(--fd);color:var(--gold);font-size:clamp(.84rem,2.3vw,1.08rem);white-space:nowrap}

/* Answers Grid */
#answers{display:grid;grid-template-columns:1fr 1fr;gap:clamp(8px,1.8vw,12px);width:100%;flex-shrink:0;position:relative;z-index:25}
.abtn{font-family:var(--fd);font-size:clamp(.92rem,2.4vw,1.15rem);
  padding:clamp(10px,2vw,15px) clamp(12px,2.5vw,18px);
  border-radius:clamp(12px,2vw,18px);border:2px solid rgba(255,255,255,.28);
  background:rgba(10,35,70,.88);color:#fff;cursor:pointer;
  transition:all .15s;text-align:center;word-break:break-word;
  box-shadow:0 4px 14px rgba(0,0,0,.3);position:relative;z-index:25}
.abtn:hover{background:rgba(20,55,100,.95);border-color:var(--gold);transform:scale(1.02);box-shadow:0 0 16px rgba(0,245,212,.4)}
.abtn:active{transform:scale(.97)}
.abtn.ok{background:rgba(16,185,129,.9)!important;border-color:#34d399!important;box-shadow:0 0 18px #10b981}
.abtn.no{background:rgba(239,68,68,.9)!important;border-color:#f87171!important}

/* Bottom tools row */
.ebar{display:flex;align-items:center;justify-content:center;gap:12px;width:100%;flex-shrink:0;position:relative;z-index:25}
.tbtn{background:rgba(255,255,255,.15);border:1.5px solid rgba(255,255,255,.28);
  border-radius:100px;padding:6px 16px;color:#fff;font-family:var(--fb);
  font-weight:800;font-size:clamp(.78rem,2vw,.9rem);cursor:pointer;
  transition:background .2s;display:inline-flex;align-items:center;gap:6px;z-index:25}
.tbtn:hover{background:rgba(255,255,255,.26)}

/* ── SCREEN: RESULTS ── */
#sc-res{flex:1;min-height:0;overflow-y:auto;padding-bottom:16px;gap:clamp(10px,2.2vw,16px);position:relative;z-index:20}
.res-card{padding:clamp(16px,3vw,26px);text-align:center;display:flex;flex-direction:column;align-items:center;gap:10px}
.trophy{font-size:clamp(3.5rem,10vw,5rem);animation:bob 2s infinite ease-in-out alternate}
.rscore{font-family:var(--fd);font-size:clamp(2rem,6vw,3.2rem);color:var(--gold);
  text-shadow:0 0 24px rgba(255,209,102,.8)}
.tpill{font-family:var(--fd);padding:6px 20px;border-radius:100px;font-size:clamp(.95rem,2.8vw,1.25rem);letter-spacing:.4px}
.tg{background:linear-gradient(135deg,#f59e0b,#d97706);color:#fff;box-shadow:0 0 20px rgba(245,158,11,.6)}
.ts{background:linear-gradient(135deg,#94a3b8,#64748b);color:#fff;box-shadow:0 0 16px rgba(148,163,184,.5)}
.tb{background:linear-gradient(135deg,#b45309,#78350f);color:#fff;box-shadow:0 0 16px rgba(180,83,9,.5)}
.rmsg{color:rgba(255,255,255,.9);font-weight:800;font-size:clamp(.9rem,2.4vw,1.12rem);max-width:560px}

/* Near-miss Silver & Bronze Remediation Cards */
.nm-remed-card{background:rgba(255,255,255,.12);border:2px solid #38bdf8;border-radius:20px;
  padding:16px;width:100%;max-width:540px;text-align:center;display:flex;flex-direction:column;align-items:center;gap:8px}
.bronze-card{background:rgba(239,68,68,.18);border:2px solid #ef4444;border-radius:20px;
  padding:16px;width:100%;max-width:540px;text-align:center;display:flex;flex-direction:column;align-items:center;gap:8px}

/* Canvas Certificate Wrapper */
#cert-wrap{width:100%;max-width:840px;background:rgba(0,0,0,.5);border-radius:20px;
  padding:10px;box-shadow:0 16px 48px rgba(0,0,0,.7);display:flex;flex-direction:column;align-items:center;gap:10px}
#cv-cert{width:100%;height:auto;max-width:800px;border-radius:14px;box-shadow:0 8px 24px rgba(0,0,0,.5);display:block}

/* Scratchpad Modal */
#sp-modal{position:fixed;inset:0;z-index:3000;background:rgba(0,18,34,.9);backdrop-filter:blur(18px);
  display:none;flex-direction:column;align-items:center;justify-content:center;padding:12px}
#sp-modal.active{display:flex}
.sp-box{background:#041528;border:2px solid #00f5d4;border-radius:20px;width:100%;max-width:680px;
  display:flex;flex-direction:column;padding:12px;gap:10px;box-shadow:0 20px 60px rgba(0,0,0,.8)}
.sp-bar{display:flex;align-items:center;justify-content:space-between}
#cv-scratch{width:100%;height:320px;background:#020a14;border-radius:12px;border:1.5px solid rgba(255,255,255,.2);touch-action:none;cursor:crosshair}
.sp-tools{display:flex;align-items:center;gap:8px;flex-wrap:wrap}

/* Hidden Utility */
.hidden{display:none!important}
</style>
</head>
<body>
<div id="bg">
  <div class="cyber-grid"></div>

  <!-- Vibranium Fusion Containment Ring (Dark Matter Plasma Core) -->
  <div class="fusion-core-wrap">
    <svg class="fusion-svg" viewBox="0 0 200 200">
      <defs>
        <radialGradient id="plasmaGrad" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="#ffffff"/>
          <stop offset="25%" stop-color="#00f5d4"/>
          <stop offset="60%" stop-color="#a855f7"/>
          <stop offset="100%" stop-color="#0d1b3e" stop-opacity="0"/>
        </radialGradient>
        <filter id="coreGlow" x="-30%" y="-30%" width="160%" height="160%">
          <feGaussianBlur stdDeviation="4" result="blur"/>
          <feComposite in="SourceGraphic" in2="blur" operator="over"/>
        </filter>
      </defs>
      <!-- Outer Magnetic Containment Ring (Clockwise) -->
      <g class="rot-ring-cw">
        <circle cx="100" cy="100" r="88" fill="none" stroke="rgba(0,245,212,0.45)" stroke-width="2" stroke-dasharray="14 8 4 8"/>
        <circle cx="100" cy="100" r="76" fill="none" stroke="rgba(168,85,247,0.5)" stroke-width="1.5" stroke-dasharray="8 6"/>
        <!-- Emitter nodes -->
        <circle cx="100" cy="12" r="3.5" fill="#00f5d4"/>
        <circle cx="100" cy="188" r="3.5" fill="#00f5d4"/>
        <circle cx="12" cy="100" r="3.5" fill="#a855f7"/>
        <circle cx="188" cy="100" r="3.5" fill="#a855f7"/>
      </g>
      <!-- Inner Stator Ring (Counter-Clockwise) -->
      <g class="rot-ring-ccw">
        <circle cx="100" cy="100" r="62" fill="none" stroke="rgba(255,209,102,0.6)" stroke-width="2.5" stroke-dasharray="24 12"/>
        <polygon points="100,42 104,50 96,50" fill="#ffd166"/>
        <polygon points="100,158 104,150 96,150" fill="#ffd166"/>
        <polygon points="42,100 50,104 50,96" fill="#ffd166"/>
        <polygon points="158,100 150,104 150,96" fill="#ffd166"/>
      </g>
      <!-- Vibranium Plasma Orb -->
      <circle cx="100" cy="100" r="36" fill="url(#plasmaGrad)" filter="url(#coreGlow)"/>
      <circle cx="100" cy="100" r="16" fill="#ffffff" opacity="0.9"/>
    </svg>
  </div>

  <!-- Big Glowing Glass Condenser Tubes (Left & Right Flanks) -->
  <div class="condenser-tube left">
    <div class="tube-glass">
      <div class="tube-liquid"></div>
      <!-- Internal Coiled Spiral -->
      <svg class="spiral-svg" viewBox="0 0 50 400" preserveAspectRatio="none">
        <path d="M 25 0 Q 42 20 25 40 Q 8 60 25 80 Q 42 100 25 120 Q 8 140 25 160 Q 42 180 25 200 Q 8 220 25 240 Q 42 260 25 280 Q 8 300 25 320 Q 42 340 25 360 Q 8 380 25 400" fill="none" stroke="rgba(255,255,255,0.7)" stroke-width="3"/>
      </svg>
      <!-- Bubbles -->
      <div class="tube-bubble" style="width:7px;height:7px;left:35%;--dur:3.2s;--del:0.2s;--drift:5px"></div>
      <div class="tube-bubble" style="width:10px;height:10px;left:50%;--dur:4.5s;--del:1.2s;--drift:-6px"></div>
      <div class="tube-bubble" style="width:6px;height:6px;left:25%;--dur:2.8s;--del:2.1s;--drift:4px"></div>
      <div class="tube-bubble" style="width:8px;height:8px;left:60%;--dur:3.8s;--del:0.8s;--drift:-4px"></div>
    </div>
  </div>

  <div class="condenser-tube right">
    <div class="tube-glass">
      <div class="tube-liquid"></div>
      <!-- Internal Coiled Spiral -->
      <svg class="spiral-svg" viewBox="0 0 50 400" preserveAspectRatio="none">
        <path d="M 25 0 Q 8 20 25 40 Q 42 60 25 80 Q 8 100 25 120 Q 42 140 25 160 Q 8 180 25 200 Q 42 220 25 240 Q 8 260 25 280 Q 42 300 25 320 Q 8 340 25 360 Q 42 380 25 400" fill="none" stroke="rgba(255,255,255,0.7)" stroke-width="3"/>
      </svg>
      <!-- Bubbles -->
      <div class="tube-bubble" style="width:8px;height:8px;left:40%;--dur:3.6s;--del:0.4s;--drift:-5px"></div>
      <div class="tube-bubble" style="width:6px;height:6px;left:60%;--dur:2.9s;--del:1.5s;--drift:4px"></div>
      <div class="tube-bubble" style="width:11px;height:11px;left:30%;--dur:4.8s;--del:2.3s;--drift:-6px"></div>
    </div>
  </div>

  <!-- Holographic Chalkboard Science Equations in Neon Glow -->
  <div class="holo-eq" style="top:8%;left:11%;--d:5.5s;--del:0s">⟨ E = mc² ⟩ 💡</div>
  <div class="holo-eq purple" style="top:15%;right:11%;--d:6.2s;--del:0.8s">[ F = m · a ] ⚡</div>
  <div class="holo-eq gold" style="top:25%;left:8%;--d:5.8s;--del:1.4s">⟨ ΔQ = mcΔT ⟩ 🔥</div>
  <div class="holo-eq lime" style="top:32%;right:9%;--d:6.8s;--del:2.0s">[ F_g = G(m₁m₂)/r² ] 🪐</div>
  <div class="holo-eq" style="top:44%;left:7%;--d:7.2s;--del:0.5s">⟨ C₆H₁₂O₆ + 6O₂ ➔ 6CO₂ + 6H₂O ⟩ 🍃</div>
  <div class="holo-eq purple" style="top:52%;right:8%;--d:6.0s;--del:1.7s">[ ∇ · B = 0 ] 🧲</div>

  <!-- Floating animated science bubbles with neon liquid -->
  <div class="sci-bubble" style="width:38px;height:38px;top:22%;left:24%;--dur:5.2s;--del:0s"></div>
  <div class="sci-bubble" style="width:30px;height:30px;top:35%;right:22%;--dur:6.5s;--del:1.2s"></div>
  <div class="sci-bubble" style="width:44px;height:44px;top:54%;left:18%;--dur:7s;--del:2s"></div>
  <div class="sci-bubble" style="width:32px;height:32px;top:64%;right:19%;--dur:5.5s;--del:0.8s"></div>

  <!-- Lab Stars -->
  <div class="star" style="width:6px;height:6px;top:10%;left:32%;--d:3.2s;--dl:0.5s"></div>
  <div class="star" style="width:8px;height:8px;top:14%;left:58%;--d:2.8s;--dl:1s"></div>
  <div class="star" style="width:6px;height:6px;top:20%;right:35%;--d:3.5s;--dl:0.2s"></div>
  <div class="star" style="width:7px;height:7px;top:38%;left:48%;--d:4s;--dl:1.5s"></div>

  <!-- Lab Floor Platform -->
  <div class="ground"></div>
</div>

<!-- ── APP CONTAINER ── -->
<div id="app">
  <nav id="topbar">
    <div class="brand">
      <div class="pip-badge">
        <svg viewBox="0 0 60 60" style="width:32px;height:32px">
          <!-- Mini Professor Pip Face -->
          <!-- Einstein Hair -->
          <path d="M 12 28 Q 6 16 18 10 Q 30 2 42 10 Q 54 16 48 28" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
          <!-- Mane -->
          <circle cx="30" cy="32" r="18" fill="#f59e0b"/>
          <!-- Face -->
          <circle cx="30" cy="33" r="13" fill="#fde047"/>
          <!-- Specs -->
          <circle cx="25" cy="32" r="5" fill="rgba(0,245,212,0.4)" stroke="#1e293b" stroke-width="1.5"/>
          <circle cx="35" cy="32" r="5" fill="rgba(0,245,212,0.4)" stroke="#1e293b" stroke-width="1.5"/>
          <line x1="30" y1="32" x2="30" y2="32" stroke="#1e293b" stroke-width="1.5"/>
          <circle cx="25" cy="32" r="1.8" fill="#1e293b"/>
          <circle cx="35" cy="32" r="1.8" fill="#1e293b"/>
          <!-- Smile -->
          <path d="M 27 38 Q 30 42 33 38" stroke="#1e293b" stroke-width="1.5" fill="none" stroke-linecap="round"/>
        </svg>
      </div>
      <h1>Safari Science Quest</h1>
    </div>
    <div class="topright">
      <div class="stamp" id="stamp">🎫 Lab Passport Stamped</div>
      <button class="ppill" onclick="changeName()">
        <span style="font-size:1.15rem">🧭</span>
        <span class="pnm" id="disp-name">Young Scientist</span>
        <span style="font-size:.7rem;opacity:.7">✏️</span>
      </button>
    </div>
  </nav>

  <div id="main">

    <!-- SCREEN 1: START SCREEN -->
    <section class="screen active" id="sc-start">
      <div class="hero">
        <div class="hero-pip-wrap">
          <svg viewBox="0 0 120 120" style="width:100%;height:100%">
            <!-- Full Professor Pip Mascot with Einstein Hair, Specs, Lab Coat & Flask -->
            <defs>
              <linearGradient id="pipCoat" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#ffffff"/>
                <stop offset="100%" stop-color="#e2e8f0"/>
              </linearGradient>
              <linearGradient id="pipFlask" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#00f5d4"/>
                <stop offset="100%" stop-color="#10b981"/>
              </linearGradient>
            </defs>
            <!-- Wild Einstein Hair Shock -->
            <path d="M 25 55 C 10 40 10 20 28 14 C 36 6 52 4 60 10 C 68 4 84 6 92 14 C 110 20 110 40 95 55 C 108 42 104 22 88 18 C 76 8 44 8 32 18 C 16 22 12 42 25 55 Z" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2.5"/>
            <!-- Golden Lion Mane -->
            <circle cx="60" cy="54" r="32" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>
            <!-- Lab Coat Body -->
            <path d="M 38 82 L 32 114 L 88 114 L 82 82 Z" fill="url(#pipCoat)" stroke="#94a3b8" stroke-width="2"/>
            <!-- Lapels -->
            <polygon points="60,82 52,98 60,114" fill="#cbd5e1"/>
            <polygon points="60,82 68,98 60,114" fill="#cbd5e1"/>
            <!-- Pocket with pens -->
            <rect x="68" y="94" width="12" height="12" rx="2" fill="#e2e8f0" stroke="#94a3b8" stroke-width="1.2"/>
            <line x1="71" y1="90" x2="71" y2="94" stroke="#00f5d4" stroke-width="2" stroke-linecap="round"/>
            <line x1="75" y1="88" x2="75" y2="94" stroke="#ff70a6" stroke-width="2" stroke-linecap="round"/>
            <line x1="78" y1="91" x2="78" y2="94" stroke="#ffd166" stroke-width="1.8" stroke-linecap="round"/>
            <!-- Pip Head -->
            <circle cx="60" cy="54" r="23" fill="#fde047"/>
            <!-- Ears -->
            <circle cx="40" cy="38" r="8" fill="#f59e0b"/>
            <circle cx="40" cy="38" r="5" fill="#fde047"/>
            <circle cx="80" cy="38" r="8" fill="#f59e0b"/>
            <circle cx="80" cy="38" r="5" fill="#fde047"/>
            <!-- Round Scientist Spectacles (Glowing Neon Cyan) -->
            <circle cx="51" cy="53" r="9.5" fill="rgba(0,245,212,0.3)" stroke="#00f5d4" stroke-width="2.5"/>
            <circle cx="69" cy="53" r="9.5" fill="rgba(0,245,212,0.3)" stroke="#00f5d4" stroke-width="2.5"/>
            <line x1="60.5" y1="53" x2="59.5" y2="53" stroke="#00f5d4" stroke-width="2.5"/>
            <!-- Big Eyes inside Specs -->
            <circle cx="51" cy="53" r="3.6" fill="#1e293b"/>
            <circle cx="69" cy="53" r="3.6" fill="#1e293b"/>
            <circle cx="52.5" cy="51.5" r="1.4" fill="#ffffff"/>
            <circle cx="70.5" cy="51.5" r="1.4" fill="#ffffff"/>
            <!-- Nose & Cheerful Whiskers -->
            <ellipse cx="60" cy="60" rx="3.5" ry="2.5" fill="#f43f5e"/>
            <path d="M 55 64 Q 60 69 65 64" stroke="#1e293b" stroke-width="2" fill="none" stroke-linecap="round"/>
            <!-- Bubbling Erlenmeyer Flask held in right paw -->
            <g transform="translate(80, 84)">
              <polygon points="12,4 16,4 16,14 26,28 2,28 12,14" fill="rgba(255,255,255,0.25)" stroke="#38bdf8" stroke-width="1.8"/>
              <polygon points="13,18 24,27 4,27 13,18" fill="url(#pipFlask)"/>
              <!-- Bubbles emerging -->
              <circle cx="14" cy="2" r="2.5" fill="#00f5d4" opacity="0.9"/>
              <circle cx="19" cy="-4" r="3" fill="#10b981" opacity="0.8"/>
            </g>
          </svg>
        </div>
        <h2>Safari Science Quest</h2>
        <p>MEP Prathomsuksa 3 · Professor Pip's Einstein Quantum Lab & Exam</p>
      </div>
      <div class="mode-grid">
        <!-- Mode 1: Professor Pip's Discovery Labs -->
        <div class="glass card mcard">
          <div class="mi">🔬💡</div>
          <div class="mt">Discovery Labs</div>
          <div class="md">5 interactive classroom labs · hands-on experiments & discovery games</div>
          <button class="btn bpu full" style="margin-top:6px;font-size:clamp(1.02rem,3vw,1.25rem);padding:clamp(12px,2.5vw,16px) 20px" onclick="goTrain()">Enter Einstein's Lab 🧪</button>
          <div class="ml">Complete all 5 labs → unlock Exam Mode</div>
        </div>

        <!-- Mode 2: Exam Challenge -->
        <div class="glass card mcard">
          <div class="mi">⚔️🏆</div>
          <div class="mt">Exam Challenge</div>
          <div class="md">15 graded questions covering curriculum · earn your Gold Certificate!</div>
          <button class="btn bg full" style="margin-top:6px;font-size:clamp(1.02rem,3vw,1.25rem);padding:clamp(12px,2.5vw,16px) 20px" id="btn-exam" onclick="startExam()">Start Science Exam 🏆</button>
          <div class="ml" id="exam-lock">🔒 Complete all 5 Discovery Labs first</div>
        </div>
      </div>
    </section>

    <!-- SCREEN 2: PROFESSOR PIP'S EINSTEIN DISCOVERY LABS (MODE 1) -->
    <section class="screen" id="sc-train">
      <!-- Hub of 5 Labs -->
      <div id="camp-hub" style="display:flex;flex-direction:column;flex:1;min-height:0;gap:clamp(8px,2vw,12px)">
        <div class="tbar">
          <button class="bk" onclick="goHome()">← Home</button>
          <span class="tbar-title">🧪 Professor Pip's Discovery Labs</span>
        </div>
        <div class="camps" id="camp-grid">
          <div class="glass card camp" onclick="startCamp(0)">
            <div class="ci">🥗</div>
            <div class="cn">Living Needs</div>
            <div class="cd">Carbs for energy, Protein for growth, Vitamins for health</div>
            <div class="cs" id="cs0">⬜</div>
          </div>
          <div class="glass card camp" onclick="startCamp(1)">
            <div class="ci">🐯</div>
            <div class="cn">Animal Diets</div>
            <div class="cd">Herbivore, Carnivore & Omnivore lunch</div>
            <div class="cs" id="cs1">⬜</div>
          </div>
          <div class="glass card camp" onclick="startCamp(2)">
            <div class="ci">🦋</div>
            <div class="cn">Life Cycle Studio</div>
            <div class="cd">Chicken, Butterfly, Frog & Human stages</div>
            <div class="cs" id="cs2">⬜</div>
          </div>
          <div class="glass card camp" onclick="startCamp(3)">
            <div class="ci">🍫</div>
            <div class="cn">The Thermal Lab</div>
            <div class="cd">Melting chocolate in pan, freezing & irreversible egg</div>
            <div class="cs" id="cs3">⬜</div>
          </div>
          <div class="glass card camp" onclick="startCamp(4)">
            <div class="ci">🧲</div>
            <div class="cn">Forces & Magnets</div>
            <div class="cd">Push/Pull, Ramp Friction & Magnets Attract/Repel</div>
            <div class="cs" id="cs4">⬜</div>
          </div>
        </div>
      </div>

      <!-- Interactive Lab Play Arena -->
      <div id="t-prac">
        <div class="tbar">
          <button class="bk" onclick="backCamps()">← All Labs</button>
          <span class="tbar-title" id="t-ctitle">🔬 Lab Arena</span>
          <span style="color:var(--gold);font-family:var(--fd);font-size:clamp(.85rem,2.2vw,1.05rem);margin-left:auto" id="t-prog">Step 1 / 3</span>
        </div>

        <div class="glass card" id="lab-card">
          <div class="lab-badge" id="lab-badge">EXPERIMENT 1</div>
          <div id="lab-prompt"></div>
          
          <!-- Spotlight display container with generous breathing room -->
          <div id="lab-disp"></div>
          
          <!-- Choices Row -->
          <div class="lab-choices" id="lab-choices"></div>

          <!-- Success & Learn Banner -->
          <div class="lab-success-banner" id="lab-success">
            <div style="font-size:1.8rem">🌟</div>
            <div class="lab-success-txt" id="lab-success-txt"></div>
            <button class="btn btn-gold" id="lab-next-btn" onclick="nextCampStep()">Next Step ➔</button>
          </div>
        </div>

        <div class="ebar">
          <button class="tbtn" onclick="tAudio()">🔊 Hear Teacher</button>
          <button class="tbtn" onclick="openSP()">✏️ Scratchpad</button>
        </div>
      </div>

      <!-- Camp Completed Card (With Linear Progression to Next Lab) -->
      <div id="t-done" class="glass card hidden" style="padding:clamp(16px,3vw,28px);flex:1;align-items:center;justify-content:center;text-align:center;gap:12px">
        <div style="font-size:clamp(3.2rem,8vw,4.8rem)">🎉🧪</div>
        <h2 style="font-family:var(--fd);color:var(--gold);font-size:clamp(1.5rem,4vw,2.2rem)">Lab Experiment Complete!</h2>
        <p id="t-done-score" style="font-size:clamp(.9rem,2.5vw,1.1rem);font-weight:700"></p>
        <p style="color:#6ee7b7;font-size:clamp(.85rem,2.2vw,1rem);font-weight:800">🎫 Lab Passport Stamped with a Gold Star!</p>
        
        <!-- Action buttons with Next Lab flow -->
        <div style="display:flex;gap:10px;margin-top:10px;flex-wrap:wrap;justify-content:center">
          <button class="btn bg" id="btn-next-lab" onclick="goNextLab()">Next Lab ➔</button>
          <button class="btn bb" onclick="backCamps()">All Labs 🏕️</button>
          <button class="btn btn-gold" id="t-done-exam-btn" onclick="startExam()">Start Science Exam 🏆</button>
        </div>
      </div>
    </section>

    <!-- SCREEN 3: EXAM CHALLENGE (MODE 2) -->
    <section class="screen" id="sc-exam">
      <div class="prow">
        <span class="qlbl" id="q-lbl">Q 1 / 15</span>
        <div class="ptrack"><div class="pfill" id="pfill" style="width:0%"></div></div>
        <span class="slbl" id="s-lbl">⭐ 0</span>
      </div>
      <div class="glass card" id="qcard">
        <div class="zbadge" id="zbadge">Zone A · Question</div>
        <div id="q-prompt"></div>
        <div id="q-disp"></div>
      </div>
      <div id="answers"></div>
      <div class="ebar">
        <button class="tbtn" onclick="eAudio()">🔊 Hear Question</button>
        <button class="tbtn" onclick="openSP()">✏️ Scratchpad</button>
      </div>
    </section>

    <!-- SCREEN 4: RESULTS & CERTIFICATE -->
    <section class="screen" id="sc-res">
      <div class="glass card res-card">
        <div class="trophy" id="r-trophy">🏆</div>
        <div class="rscore" id="r-score">15 / 15</div>
        <div class="tpill tg" id="r-tier">👑 GOLD MASTER!</div>
        <p class="rmsg" id="r-msg">Incredible work! You are a certified Safari Science Champion!</p>

        <!-- Near-miss Silver Remediation Card -->
        <div class="nm-remed-card hidden" id="nearmiss">
          <div style="font-size:1.6rem">🌟 Silver Explorer!</div>
          <p id="nm-desc" style="font-size:.9rem;font-weight:700;color:rgba(255,255,255,.9)"></p>
          <div style="display:flex;gap:10px;margin-top:6px;flex-wrap:wrap;justify-content:center">
            <button class="btn bg" id="btn-awaken">Retry Missed Questions ⚡</button>
            <button class="btn bb" onclick="toggleSilverCert(true)">View Silver Diploma 📜</button>
          </div>
        </div>

        <!-- Bronze Remediation Card ("Bronze is not acceptable") -->
        <div class="bronze-card hidden" id="bronzecard">
          <div style="font-size:1.6rem">🧭 Science Training Needed</div>
          <p id="bc-desc" style="font-size:.9rem;font-weight:700;color:rgba(255,255,255,.92)">Every great scientist learns through experiments! Let's return to the Discovery Labs to practice before retaking the Exam.</p>
          <button class="btn bo" id="btn-retrain" onclick="goTrain()" style="margin-top:6px">Enter Discovery Lab 🧪</button>
        </div>

        <!-- Canvas Certificate Container -->
        <div id="certsec" class="hidden" style="width:100%;display:flex;flex-direction:column;align-items:center;gap:12px;margin-top:12px">
          <div id="cert-wrap">
            <canvas id="cv-cert"></canvas>
          </div>
          <div style="display:flex;gap:10px;flex-wrap:wrap;justify-content:center">
            <button class="btn bb" id="btn-dl" onclick="dlCert()">💾 Save Certificate (PNG)</button>
            <button class="btn bg" onclick="window.print()">🖨️ Print Certificate</button>
            <button class="btn bo" onclick="goHome()">🏠 Base Camp</button>
            <button class="btn bpu" onclick="startExam()">🔄 Retake Exam</button>
          </div>
        </div>
      </div>
    </section>

  </div>
</div>

<!-- ── NAME MODAL ── -->
<div id="name-modal">
  <div class="nm-card">
    <div class="nm-pip-avatar">
      <svg viewBox="0 0 120 120" style="width:100%;height:100%">
        <!-- Wild Einstein Hair Shock -->
        <path d="M 25 55 C 10 40 10 20 28 14 C 36 6 52 4 60 10 C 68 4 84 6 92 14 C 110 20 110 40 95 55 C 108 42 104 22 88 18 C 76 8 44 8 32 18 C 16 22 12 42 25 55 Z" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2.5"/>
        <!-- Golden Lion Mane -->
        <circle cx="60" cy="54" r="32" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>
        <!-- Pip Head -->
        <circle cx="60" cy="54" r="23" fill="#fde047"/>
        <!-- Ears -->
        <circle cx="40" cy="38" r="8" fill="#f59e0b"/>
        <circle cx="40" cy="38" r="5" fill="#fde047"/>
        <circle cx="80" cy="38" r="8" fill="#f59e0b"/>
        <circle cx="80" cy="38" r="5" fill="#fde047"/>
        <!-- Round Scientist Spectacles (Glowing Neon Cyan) -->
        <circle cx="51" cy="53" r="9.5" fill="rgba(0,245,212,0.3)" stroke="#00f5d4" stroke-width="2.5"/>
        <circle cx="69" cy="53" r="9.5" fill="rgba(0,245,212,0.3)" stroke="#00f5d4" stroke-width="2.5"/>
        <line x1="60.5" y1="53" x2="59.5" y2="53" stroke="#00f5d4" stroke-width="2.5"/>
        <circle cx="51" cy="53" r="3.6" fill="#1e293b"/>
        <circle cx="69" cy="53" r="3.6" fill="#1e293b"/>
        <circle cx="52.5" cy="51.5" r="1.4" fill="#ffffff"/>
        <circle cx="70.5" cy="51.5" r="1.4" fill="#ffffff"/>
        <ellipse cx="60" cy="60" rx="3.5" ry="2.5" fill="#f43f5e"/>
        <path d="M 55 64 Q 60 69 65 64" stroke="#1e293b" stroke-width="2" fill="none" stroke-linecap="round"/>
      </svg>
    </div>
    <h2>Young Scientist!</h2>
    <p>Welcome to Professor Pip's Einstein Quantum Lab! Enter your name to customize your official diploma:</p>
    <input type="text" id="nm-input" maxlength="24" placeholder="Your Name" autocomplete="off" autocorrect="off">
    <button class="btn btn-gold full" onclick="submitName()">Start Scientific Adventure 🚀</button>
  </div>
</div>

<!-- ── SCRATCHPAD MODAL ── -->
<div id="sp-modal">
  <div class="sp-box">
    <div class="sp-bar">
      <span style="font-family:var(--fd);color:var(--gold);font-size:1.15rem">✏️ Science Lab Scratchpad</span>
      <button class="bk" onclick="closeSP()">✕ Close</button>
    </div>
    <canvas id="cv-scratch" width="650" height="320"></canvas>
    <div class="sp-tools">
      <button class="btn" style="background:#38bdf8;padding:6px 14px;font-size:.85rem" onclick="CA.setC('#38bdf8')">Cyan</button>
      <button class="btn" style="background:#fbbf24;color:#78350f;padding:6px 14px;font-size:.85rem" onclick="CA.setC('#fbbf24')">Gold</button>
      <button class="btn" style="background:#34d399;padding:6px 14px;font-size:.85rem" onclick="CA.setC('#34d399')">Mint</button>
      <button class="btn" style="background:#ffffff;color:#000;padding:6px 14px;font-size:.85rem" onclick="CA.setC('#ffffff')">White</button>
      <button class="btn bpk" style="padding:6px 14px;font-size:.85rem" onclick="CA.setEraser(true)">Eraser</button>
      <button class="btn bo" style="padding:6px 14px;font-size:.85rem;margin-left:auto" onclick="CA.clr()">Clear All</button>
    </div>
  </div>
</div>

<script>
/* ============================================================ AUDIO SYNTHESIZER & SPEECH */
const CA = (function(){
  let ac = null, st = null;
  function gac(){
    if(!ac){
      const C = window.AudioContext || window.webkitAudioContext;
      if(C) ac = new C();
    }
    if(ac && ac.state === 'suspended') ac.resume();
    return ac;
  }
  function findFemaleVoice(vs){
    if(!vs || !vs.length) return null;
    const pool = vs.filter(v => v.lang && v.lang.toLowerCase().startsWith('en'));
    const list = pool.length ? pool : vs;
    const fNames = ['zira','jenny','aria','samantha','victoria','karen','fiona','moira','tessa','veena','female','woman','girl','catherine','susan','linda','hazel','stephanie','ava','allison','serena'];
    let chosen = list.find(v => {
      const nm = v.name.toLowerCase();
      return fNames.some(fn => nm.includes(fn)) || (nm.includes('google') && nm.includes('female'));
    });
    if(chosen) return chosen;
    const mNames = ['david','mark','guy','george','james','male','richard','sean','stefan','paul','brian'];
    chosen = list.find(v => {
      const nm = v.name.toLowerCase();
      return !mNames.some(mn => nm.includes(mn));
    });
    return chosen || list[0];
  }
  function spk(t, immediate=false){
    if(!('speechSynthesis' in window) || !t) return;
    if(st){ clearTimeout(st); st = null; }
    try{
      if(window.speechSynthesis.paused) window.speechSynthesis.resume();
      window.speechSynthesis.cancel();
    }catch(e){}
    const run = () => {
      try{
        if(window.speechSynthesis.paused) window.speechSynthesis.resume();
        const u = new SpeechSynthesisUtterance(t.trim());
        u.rate = 0.88; u.pitch = 1.15; u.lang = 'en-US';
        const vs = window.speechSynthesis.getVoices();
        const v = findFemaleVoice(vs);
        if(v) u.voice = v;
        window.speechSynthesis.speak(u);
      }catch(e){}
    };
    if(immediate) run(); else st = setTimeout(run, 200);
  }
  function nt(f, d, dur, tp='triangle', vol=0.18){
    const ctx = gac(); if(!ctx) return;
    const now = ctx.currentTime;
    const o = ctx.createOscillator(), g = ctx.createGain();
    o.type = tp; o.frequency.setValueAtTime(f, now + d);
    g.gain.setValueAtTime(0.0001, now + d);
    g.gain.linearRampToValueAtTime(vol, now + d + 0.02);
    g.gain.exponentialRampToValueAtTime(0.0001, now + d + dur);
    o.connect(g); g.connect(ctx.destination);
    o.start(now + d); o.stop(now + d + dur + 0.05);
  }
  function ok(){ [[523.25,0,.5],[659.25,.08,.5],[783.99,.16,.6],[1046.5,.24,.7]].forEach(([f,d,r])=>nt(f,d,r)); }
  function er(){ [[220,0,.2,'sawtooth',.2],[185,.15,.35,'sawtooth',.22]].forEach(([f,d,r,t,v])=>nt(f,d,r,t,v)); }
  function isp(){ [[440,0,.35],[554.37,.1,.45]].forEach(([f,d,r])=>nt(f,d,r)); }
  function fan(){
    [[523.25,0,.25],[523.25,.12,.2],[523.25,.24,.2],[659.25,.36,.4],[783.99,.52,.3],[1046.5,.7,.9]].forEach(([f,d,r])=>nt(f,d,r,'triangle',.22));
  }
  let spCtx=null,drw=false,lx=0,ly=0,sc='#38bdf8',isErasing=false;
  function initSP(){
    const cv=document.getElementById('cv-scratch');if(!cv)return;
    spCtx=cv.getContext('2d');
    const pos=e=>{const r=cv.getBoundingClientRect();const cx=e.touches?e.touches[0].clientX:e.clientX;const cy=e.touches?e.touches[0].clientY:e.clientY;return{x:cx-r.left,y:cy-r.top};};
    const st2=e=>{drw=true;const p=pos(e);lx=p.x;ly=p.y;};
    const dr=e=>{
      if(!drw||!spCtx)return;if(e.touches)e.preventDefault();
      const p=pos(e);spCtx.beginPath();spCtx.moveTo(lx,ly);spCtx.lineTo(p.x,p.y);spCtx.lineCap='round';spCtx.lineJoin='round';
      if(isErasing){spCtx.globalCompositeOperation='destination-out';spCtx.lineWidth=24;}
      else{spCtx.globalCompositeOperation='source-over';spCtx.lineWidth=4;spCtx.strokeStyle=sc;}
      spCtx.stroke();lx=p.x;ly=p.y;
    };
    const en=()=>{drw=false;};
    cv.addEventListener('mousedown',st2);cv.addEventListener('mousemove',dr);cv.addEventListener('mouseup',en);cv.addEventListener('mouseleave',en);
    cv.addEventListener('touchstart',st2,{passive:false});cv.addEventListener('touchmove',dr,{passive:false});cv.addEventListener('touchend',en,{passive:false});
  }
  function clr(){const cv=document.getElementById('cv-scratch');if(cv&&spCtx)spCtx.clearRect(0,0,cv.width,cv.height);}
  return { spk, ok, er, isp, fan, initSP, clr, setC: c=>{sc=c;isErasing=false;}, setEraser: e=>{isErasing=e;}, gac };
})();

/* ============================================================ SCIENCE ENGINE */
const SE = (function(){
  const ri = (a, b) => Math.floor(Math.random() * (b - a + 1)) + a;
  const sh = a => [...a].sort(() => Math.random() - 0.5);

  /* SVG DIAGRAM GENERATORS (HIGH-FIDELITY, LARGE, GEEK-SCIENCE LAB GRAPHICS) */
  const SVG = {
    // Both Bread AND Rice clearly shown together (Large, rich culinary science illustration)
    carbsBreadAndRice: () => `
      <div class="disp-spotlight">
        <svg viewBox="0 0 460 135">
          <defs>
            <linearGradient id="crustGrad" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#b45309"/>
              <stop offset="40%" stop-color="#d97706"/>
              <stop offset="100%" stop-color="#78350f"/>
            </linearGradient>
            <linearGradient id="breadInside" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#fffbeb"/>
              <stop offset="100%" stop-color="#fef3c7"/>
            </linearGradient>
            <linearGradient id="bowlGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#0284c7"/>
              <stop offset="100%" stop-color="#0369a1"/>
            </linearGradient>
          </defs>

          <!-- Golden Bread Loaf & Slices (Left) -->
          <g transform="translate(45, 10)">
            <!-- Cutting Board -->
            <rect x="0" y="80" width="145" height="12" rx="4" fill="#92400e" stroke="#78350f" stroke-width="1.5"/>
            <!-- Main Loaf -->
            <ellipse cx="65" cy="52" rx="55" ry="34" fill="url(#crustGrad)" stroke="#78350f" stroke-width="2"/>
            <!-- Baker Scores -->
            <path d="M 28 50 Q 65 24 102 50" fill="url(#breadInside)" stroke="#b45309" stroke-width="1.8"/>
            <line x1="45" y1="36" x2="45" y2="60" stroke="#92400e" stroke-width="2.5" stroke-linecap="round"/>
            <line x1="65" y1="32" x2="65" y2="64" stroke="#92400e" stroke-width="2.5" stroke-linecap="round"/>
            <line x1="85" y1="36" x2="85" y2="60" stroke="#92400e" stroke-width="2.5" stroke-linecap="round"/>
            <!-- Sliced Bread falling beside loaf -->
            <g transform="translate(100, 40) rotate(14)">
              <ellipse cx="14" cy="18" rx="13" ry="18" fill="url(#breadInside)" stroke="#b45309" stroke-width="2"/>
            </g>
            <text x="72" y="108" font-size="12" font-weight="900" fill="#fde68a" text-anchor="middle" font-family="var(--fd)">CRUSTY BREAD 🍞</text>
          </g>

          <!-- Central Energy Fusion Plus Symbol -->
          <g transform="translate(230, 54)">
            <circle cx="0" cy="0" r="16" fill="rgba(255,209,102,0.18)" stroke="#ffd166" stroke-width="2"/>
            <text x="0" y="7" font-size="24" font-weight="bold" fill="#ffd166" text-anchor="middle" font-family="var(--fd)">+</text>
          </g>

          <!-- Steaming Jasmine Rice Bowl with Chopsticks (Right) -->
          <g transform="translate(265, 10)">
            <!-- Steam Curls rising into air -->
            <path d="M 50 16 Q 44 4 52 -6 Q 60 -16 52 -22" stroke="rgba(255,255,255,0.75)" stroke-width="2.5" fill="none" stroke-linecap="round"/>
            <path d="M 72 12 Q 78 0 70 -10 Q 62 -20 72 -26" stroke="rgba(255,255,255,0.75)" stroke-width="3" fill="none" stroke-linecap="round"/>
            <path d="M 94 16 Q 88 4 96 -6 Q 104 -16 96 -22" stroke="rgba(255,255,255,0.75)" stroke-width="2.5" fill="none" stroke-linecap="round"/>
            <!-- Rice Mound -->
            <ellipse cx="72" cy="46" rx="52" ry="24" fill="#ffffff" stroke="#e2e8f0" stroke-width="2"/>
            <!-- Rice Grain Texture -->
            <circle cx="58" cy="42" r="2.2" fill="#cbd5e1"/>
            <circle cx="72" cy="38" r="2.2" fill="#cbd5e1"/>
            <circle cx="86" cy="42" r="2.2" fill="#cbd5e1"/>
            <circle cx="68" cy="48" r="2.2" fill="#cbd5e1"/>
            <!-- Ceramic Patterned Bowl -->
            <path d="M 20 46 Q 72 105 124 46 Z" fill="url(#bowlGrad)" stroke="#0284c7" stroke-width="2.5"/>
            <!-- Bowl Base -->
            <rect x="52" y="86" width="40" height="7" rx="3" fill="#0369a1"/>
            <!-- Chopsticks Resting across bowl -->
            <line x1="24" y1="28" x2="135" y2="48" stroke="#f59e0b" stroke-width="3" stroke-linecap="round"/>
            <line x1="20" y1="36" x2="132" y2="54" stroke="#d97706" stroke-width="3" stroke-linecap="round"/>
            <text x="72" y="108" font-size="12" font-weight="900" fill="#fde68a" text-anchor="middle" font-family="var(--fd)">STEAMING RICE 🍚</text>
          </g>
        </svg>
      </div>
      <div class="disp-pill">⚡ CARBOHYDRATE · PRIMARY FUEL FOR BODY ENERGY</div>
    `,

    // Protein Foods (Steak, Salmon Fillet & Eggs)
    proteinFoods: () => `
      <div class="disp-spotlight">
        <svg viewBox="0 0 460 135">
          <!-- Steak on wooden platter -->
          <g transform="translate(60, 15)">
            <ellipse cx="60" cy="50" rx="54" ry="32" fill="#dc2626" stroke="#991b1b" stroke-width="2.5"/>
            <circle cx="48" cy="45" r="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
            <ellipse cx="78" cy="52" rx="22" ry="12" fill="#b91c1c" opacity="0.6"/>
            <!-- Grill lines -->
            <line x1="30" y1="40" x2="90" y2="48" stroke="#7f1d1d" stroke-width="2.5" stroke-linecap="round"/>
            <line x1="35" y1="52" x2="85" y2="60" stroke="#7f1d1d" stroke-width="2.5" stroke-linecap="round"/>
            <text x="60" y="98" font-size="12" font-weight="900" fill="#fca5a5" text-anchor="middle" font-family="var(--fd)">BEEF STEAK 🥩</text>
          </g>

          <g transform="translate(230, 54)">
            <circle cx="0" cy="0" r="16" fill="rgba(0,245,212,0.18)" stroke="#00f5d4" stroke-width="2"/>
            <text x="0" y="7" font-size="24" font-weight="bold" fill="#00f5d4" text-anchor="middle" font-family="var(--fd)">+</text>
          </g>

          <!-- Fresh Fish / Salmon Fillet -->
          <g transform="translate(270, 15)">
            <ellipse cx="65" cy="50" rx="56" ry="24" fill="#38bdf8" stroke="#0284c7" stroke-width="2.5"/>
            <!-- Tail -->
            <polygon points="118,50 142,32 142,68" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
            <!-- Fin -->
            <path d="M 60 26 Q 72 16 78 26 Z" fill="#0284c7"/>
            <circle cx="36" cy="46" r="4.5" fill="#0f172a"/>
            <circle cx="37" cy="44.5" r="1.5" fill="#fff"/>
            <text x="65" y="98" font-size="12" font-weight="900" fill="#7dd3fc" text-anchor="middle" font-family="var(--fd)">SALMON & FISH 🐟</text>
          </g>
        </svg>
      </div>
      <div class="disp-pill">💪 PROTEIN · HELPS BODY GROW & BUILDS STRONG MUSCLES</div>
    `,

    // Vitamins & Minerals (Apple & Fresh Carrot)
    vitaminFoods: () => `
      <div class="disp-spotlight">
        <svg viewBox="0 0 460 135">
          <!-- Big Ruby Apple -->
          <g transform="translate(90, 15)">
            <circle cx="50" cy="50" r="36" fill="#ef4444" stroke="#991b1b" stroke-width="2.5"/>
            <path d="M 50 16 Q 58 4 64 8" stroke="#78350f" stroke-width="4" fill="none" stroke-linecap="round"/>
            <ellipse cx="64" cy="18" rx="10" ry="5" fill="#22c55e" stroke="#15803d" stroke-width="1.5" transform="rotate(-20 64 18)"/>
            <text x="50" y="100" font-size="12" font-weight="900" fill="#86efac" text-anchor="middle" font-family="var(--fd)">FRESH APPLE 🍎</text>
          </g>

          <g transform="translate(230, 54)">
            <circle cx="0" cy="0" r="16" fill="rgba(16,185,129,0.2)" stroke="#10b981" stroke-width="2"/>
            <text x="0" y="7" font-size="24" font-weight="bold" fill="#10b981" text-anchor="middle" font-family="var(--fd)">+</text>
          </g>

          <!-- Crisp Orange Carrot -->
          <g transform="translate(275, 12)">
            <g transform="rotate(32 60 50)">
              <polygon points="60,20 74,75 46,75" fill="#f97316" stroke="#c2410c" stroke-width="2.5"/>
              <line x1="52" y1="40" x2="68" y2="40" stroke="#c2410c" stroke-width="2" stroke-linecap="round"/>
              <line x1="55" y1="55" x2="65" y2="55" stroke="#c2410c" stroke-width="2" stroke-linecap="round"/>
              <!-- Green top -->
              <path d="M 60 20 Q 55 2 50 0 M 60 20 Q 60 0 62 -4 M 60 20 Q 65 2 72 2" stroke="#22c55e" stroke-width="3.5" fill="none" stroke-linecap="round"/>
            </g>
            <text x="60" y="102" font-size="12" font-weight="900" fill="#86efac" text-anchor="middle" font-family="var(--fd)">CRUNCHY CARROT 🥕</text>
          </g>
        </svg>
      </div>
      <div class="disp-pill">🛡️ VITAMINS · KEEPS IMMUNE SYSTEM HEALTHY & STRONG</div>
    `,

    // Large, Cute Detailed Spotted Cow Chewing Lush Grass
    cowEatingGrass: () => `
      <div class="disp-spotlight">
        <svg viewBox="0 0 460 135">
          <!-- Pasture Field Mound -->
          <ellipse cx="230" cy="120" rx="210" ry="24" fill="#065f46" stroke="#10b981" stroke-width="1.8"/>

          <!-- Detailed Cute Dairy Cow (Left) -->
          <g transform="translate(70, 10)">
            <!-- Tail -->
            <path d="M 28 65 Q 12 70 16 85" stroke="#475569" stroke-width="3" fill="none"/>
            <circle cx="16" cy="85" r="4.5" fill="#1e293b"/>
            <!-- Cow Body -->
            <ellipse cx="75" cy="62" rx="46" ry="32" fill="#ffffff" stroke="#334155" stroke-width="2.5"/>
            <!-- Body Spots -->
            <path d="M 45 52 Q 55 42 68 50 Q 62 68 48 64 Z" fill="#1e293b"/>
            <path d="M 85 45 Q 102 48 98 64 Q 82 66 85 45 Z" fill="#1e293b"/>
            <circle cx="68" cy="78" r="8" fill="#1e293b"/>
            <!-- Legs with Hooves -->
            <rect x="42" y="84" width="10" height="26" rx="3" fill="#ffffff" stroke="#334155" stroke-width="2"/>
            <rect x="42" y="104" width="10" height="6" fill="#1e293b"/>
            <rect x="60" y="84" width="10" height="26" rx="3" fill="#ffffff" stroke="#334155" stroke-width="2"/>
            <rect x="60" y="104" width="10" height="6" fill="#1e293b"/>
            <rect x="85" y="84" width="10" height="26" rx="3" fill="#ffffff" stroke="#334155" stroke-width="2"/>
            <rect x="85" y="104" width="10" height="6" fill="#1e293b"/>
            <!-- Cow Head -->
            <circle cx="118" cy="48" r="24" fill="#ffffff" stroke="#334155" stroke-width="2.5"/>
            <!-- Head Spot -->
            <path d="M 108 30 Q 124 30 120 44 Q 108 42 108 30 Z" fill="#1e293b"/>
            <!-- Horns -->
            <path d="M 110 28 Q 106 18 112 16" stroke="#ffd166" stroke-width="3" fill="none" stroke-linecap="round"/>
            <path d="M 126 28 Q 130 18 124 16" stroke="#ffd166" stroke-width="3" fill="none" stroke-linecap="round"/>
            <!-- Ears -->
            <ellipse cx="98" cy="38" rx="8" ry="4.5" fill="#fbcfe8" stroke="#334155" stroke-width="1.8" transform="rotate(-20 98 38)"/>
            <ellipse cx="138" cy="38" rx="8" ry="4.5" fill="#fbcfe8" stroke="#334155" stroke-width="1.8" transform="rotate(20 138 38)"/>
            <!-- Eyes with Sparkle -->
            <circle cx="112" cy="44" r="3.8" fill="#1e293b"/>
            <circle cx="113" cy="42.5" r="1.4" fill="#fff"/>
            <circle cx="128" cy="44" r="3.8" fill="#1e293b"/>
            <circle cx="129" cy="42.5" r="1.4" fill="#fff"/>
            <!-- Pink Snout -->
            <ellipse cx="120" cy="58" rx="16" ry="10" fill="#fbcfe8" stroke="#f472b6" stroke-width="2"/>
            <circle cx="115" cy="58" r="2.2" fill="#be185d"/>
            <circle cx="125" cy="58" r="2.2" fill="#be185d"/>
            <!-- Grass hanging from happy chewing mouth -->
            <path d="M 122 62 Q 135 68 145 64 M 122 62 Q 138 74 148 76" stroke="#22c55e" stroke-width="3" fill="none" stroke-linecap="round"/>
            <text x="75" y="125" font-size="13" font-weight="900" fill="#6ee7b7" text-anchor="middle" font-family="var(--fd)">COW 🐮</text>
          </g>

          <!-- Lush Field Grass Bushel (Right) -->
          <g transform="translate(280, 20)">
            <g stroke="#22c55e" stroke-width="4.5" stroke-linecap="round" fill="none">
              <path d="M 20 85 Q 10 40 18 10"/>
              <path d="M 32 85 Q 35 30 52 14"/>
              <path d="M 45 85 Q 52 35 68 18"/>
              <path d="M 60 85 Q 75 42 85 24"/>
              <path d="M 25 85 Q 40 45 35 22"/>
              <path d="M 50 85 Q 65 50 80 32"/>
            </g>
            <!-- Yellow Wildflowers -->
            <circle cx="18" cy="10" r="4.5" fill="#fde047"/>
            <circle cx="52" cy="14" r="4.5" fill="#fde047"/>
            <circle cx="85" cy="24" r="4.5" fill="#fde047"/>
            <text x="50" y="115" font-size="13" font-weight="900" fill="#86efac" text-anchor="middle" font-family="var(--fd)">LUSH GRASS 🌿</text>
          </g>
        </svg>
      </div>
      <div class="disp-pill">🐮 HERBIVORE · PLANT-EATING ANIMAL (EATS GRASS & LEAVES)</div>
    `,

    // Big Friendly Lion Mascot Enjoying Hearty Steak
    lionEatingMeat: () => `
      <div class="disp-spotlight">
        <svg viewBox="0 0 460 135">
          <!-- Friendly King Lion Mascot (Left) -->
          <g transform="translate(65, 12)">
            <!-- Lush Golden Mane with Depth -->
            <circle cx="65" cy="54" r="46" fill="#f59e0b" stroke="#b45309" stroke-width="2.5"/>
            <!-- Outer mane tufts -->
            <circle cx="28" cy="38" r="14" fill="#d97706"/>
            <circle cx="102" cy="38" r="14" fill="#d97706"/>
            <circle cx="28" cy="70" r="14" fill="#d97706"/>
            <circle cx="102" cy="70" r="14" fill="#d97706"/>
            <circle cx="65" cy="16" r="14" fill="#d97706"/>
            <!-- Lion Ears -->
            <circle cx="36" cy="26" r="9" fill="#f59e0b"/>
            <circle cx="36" cy="26" r="5" fill="#fde047"/>
            <circle cx="94" cy="26" r="9" fill="#f59e0b"/>
            <circle cx="94" cy="26" r="5" fill="#fde047"/>
            <!-- Lion Face -->
            <circle cx="65" cy="56" r="32" fill="#fde047"/>
            <!-- Rosy Cheeks -->
            <circle cx="44" cy="64" r="6" fill="#fb7185" opacity="0.6"/>
            <circle cx="86" cy="64" r="6" fill="#fb7185" opacity="0.6"/>
            <!-- Glowing Spectacles -->
            <circle cx="52" cy="52" r="11" fill="rgba(0,245,212,0.3)" stroke="#00f5d4" stroke-width="2.2"/>
            <circle cx="78" cy="52" r="11" fill="rgba(0,245,212,0.3)" stroke="#00f5d4" stroke-width="2.2"/>
            <line x1="63" y1="52" x2="67" y2="52" stroke="#00f5d4" stroke-width="2.2"/>
            <!-- Cheerful Eyes -->
            <circle cx="52" cy="52" r="4" fill="#1e293b"/>
            <circle cx="54" cy="50" r="1.5" fill="#ffffff"/>
            <circle cx="78" cy="52" r="4" fill="#1e293b"/>
            <circle cx="80" cy="50" r="1.5" fill="#ffffff"/>
            <!-- Nose & Mouth -->
            <polygon points="65,62 61,66 69,66" fill="#78350f"/>
            <path d="M 58 70 Q 65 76 72 70" stroke="#78350f" stroke-width="2.5" fill="none" stroke-linecap="round"/>
            <text x="65" y="118" font-size="13" font-weight="900" fill="#fde047" text-anchor="middle" font-family="var(--fd)">LION 🦁</text>
          </g>

          <!-- Prime Rib Steak with Glowing Garnish on Silver Platter (Right) -->
          <g transform="translate(255, 14)">
            <!-- Silver Serving Platter -->
            <ellipse cx="75" cy="66" rx="72" ry="26" fill="#475569" stroke="#94a3b8" stroke-width="2.5"/>
            <ellipse cx="75" cy="64" rx="66" ry="22" fill="#334155"/>
            <!-- Enormous Juicy T-Bone Steak -->
            <ellipse cx="72" cy="56" rx="52" ry="28" fill="#dc2626" stroke="#991b1b" stroke-width="2.5"/>
            <ellipse cx="76" cy="54" rx="42" ry="20" fill="#b91c1c"/>
            <!-- Bone Marrow Core -->
            <ellipse cx="50" cy="52" rx="10" ry="7" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
            <ellipse cx="50" cy="52" rx="5" ry="3.5" fill="#fde68a"/>
            <!-- Sear Grill Marks -->
            <line x1="45" y1="46" x2="105" y2="56" stroke="#7f1d1d" stroke-width="3" stroke-linecap="round"/>
            <line x1="52" y1="58" x2="98" y2="66" stroke="#7f1d1d" stroke-width="3" stroke-linecap="round"/>
            <!-- Glowing Herb Garnish -->
            <path d="M 98 42 Q 106 32 115 36 M 98 42 Q 102 28 108 26" stroke="#22c55e" stroke-width="3" fill="none" stroke-linecap="round"/>
            <!-- Aroma Steam Waves -->
            <path d="M 65 30 Q 60 18 68 8" stroke="rgba(255,209,102,0.7)" stroke-width="2.5" fill="none" stroke-linecap="round"/>
            <path d="M 85 26 Q 92 14 84 4" stroke="rgba(255,209,102,0.7)" stroke-width="2.5" fill="none" stroke-linecap="round"/>
            <text x="75" y="116" font-size="13" font-weight="900" fill="#fca5a5" text-anchor="middle" font-family="var(--fd)">PRIME STEAK 🥩</text>
          </g>
        </svg>
      </div>
      <div class="disp-pill">🦁 CARNIVORE · MEAT-EATING ANIMAL (HUNTS & CONSUMES MEAT)</div>
    `,

    // Big Chunky 3D Bar Magnets with Glowing Flux Arcs and Sparks
    magnetsAttract: () => `
      <div class="disp-spotlight">
        <svg viewBox="0 0 480 135">
          <defs>
            <linearGradient id="magRed" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#f87171"/>
              <stop offset="50%" stop-color="#ef4444"/>
              <stop offset="100%" stop-color="#991b1b"/>
            </linearGradient>
            <linearGradient id="magBlue" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#38bdf8"/>
              <stop offset="50%" stop-color="#0284c7"/>
              <stop offset="100%" stop-color="#075985"/>
            </linearGradient>
          </defs>

          <!-- Magnet 1 (Left): South [Red] - North [Blue] -->
          <g transform="translate(35, 34)">
            <!-- 3D Bevel Shadow -->
            <rect x="3" y="5" width="130" height="48" rx="8" fill="#000000" opacity="0.45"/>
            <!-- South Half (Red) -->
            <rect x="0" y="0" width="65" height="48" rx="8" fill="url(#magRed)" stroke="#7f1d1d" stroke-width="2"/>
            <text x="32" y="32" font-size="22" font-weight="900" fill="#ffffff" text-anchor="middle" font-family="var(--fd)">S</text>
            <!-- North Half (Blue) -->
            <rect x="65" y="0" width="65" height="48" rx="8" fill="url(#magBlue)" stroke="#0369a1" stroke-width="2"/>
            <text x="98" y="32" font-size="22" font-weight="900" fill="#ffffff" text-anchor="middle" font-family="var(--fd)">N</text>
            <!-- Top Highlight Gloss Strip -->
            <rect x="4" y="3" width="122" height="6" rx="3" fill="#ffffff" opacity="0.35"/>
          </g>

          <!-- Electromagnetic Energy Flux Arcs & Attraction Sparks -->
          <g transform="translate(175, 20)">
            <!-- Curved Magnetic Field Lines (Cyan & Purple Glowing) -->
            <path d="M 0 20 Q 65 -5 130 20" stroke="#00f5d4" stroke-width="2.5" fill="none" stroke-dasharray="6 4"/>
            <path d="M 0 38 Q 65 24 130 38" stroke="#a855f7" stroke-width="3" fill="none"/>
            <path d="M 0 58 Q 65 72 130 58" stroke="#a855f7" stroke-width="3" fill="none"/>
            <path d="M 0 76 Q 65 101 130 76" stroke="#00f5d4" stroke-width="2.5" fill="none" stroke-dasharray="6 4"/>
            <!-- Energy Arcs & Sparks -->
            <circle cx="65" cy="48" r="18" fill="rgba(0,245,212,0.2)" stroke="#00f5d4" stroke-width="1.8"/>
            <text x="65" y="55" font-size="26" text-anchor="middle">⚡💥⚡</text>
            <text x="65" y="86" font-size="11" font-weight="900" fill="#00f5d4" text-anchor="middle" font-family="var(--fd)">PULL TOGETHER ➔ ⬅️</text>
          </g>

          <!-- Magnet 2 (Right): South [Red] facing Magnet 1's North [Blue] -->
          <g transform="translate(315, 34)">
            <rect x="3" y="5" width="130" height="48" rx="8" fill="#000000" opacity="0.45"/>
            <!-- South Half (Red) facing Center -->
            <rect x="0" y="0" width="65" height="48" rx="8" fill="url(#magRed)" stroke="#7f1d1d" stroke-width="2"/>
            <text x="32" y="32" font-size="22" font-weight="900" fill="#ffffff" text-anchor="middle" font-family="var(--fd)">S</text>
            <!-- North Half (Blue) -->
            <rect x="65" y="0" width="65" height="48" rx="8" fill="url(#magBlue)" stroke="#0369a1" stroke-width="2"/>
            <text x="98" y="32" font-size="22" font-weight="900" fill="#ffffff" text-anchor="middle" font-family="var(--fd)">N</text>
            <rect x="4" y="3" width="122" height="6" rx="3" fill="#ffffff" opacity="0.35"/>
          </g>
        </svg>
      </div>
      <div class="disp-pill">🧲 OPPOSITE POLES (NORTH & SOUTH) ATTRACT (PULL TOGETHER)</div>
    `,

    magnetsRepel: () => `
      <div class="disp-spotlight">
        <svg viewBox="0 0 480 135">
          <defs>
            <linearGradient id="magRed2" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#f87171"/><stop offset="50%" stop-color="#ef4444"/><stop offset="100%" stop-color="#991b1b"/>
            </linearGradient>
            <linearGradient id="magBlue2" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#38bdf8"/><stop offset="50%" stop-color="#0284c7"/><stop offset="100%" stop-color="#075985"/>
            </linearGradient>
          </defs>

          <!-- Magnet 1: [S] - [N] -->
          <g transform="translate(35, 34)">
            <rect x="3" y="5" width="130" height="48" rx="8" fill="#000000" opacity="0.45"/>
            <rect x="0" y="0" width="65" height="48" rx="8" fill="url(#magRed2)" stroke="#7f1d1d" stroke-width="2"/>
            <text x="32" y="32" font-size="22" font-weight="900" fill="#ffffff" text-anchor="middle" font-family="var(--fd)">S</text>
            <rect x="65" y="0" width="65" height="48" rx="8" fill="url(#magBlue2)" stroke="#0369a1" stroke-width="2"/>
            <text x="98" y="32" font-size="22" font-weight="900" fill="#ffffff" text-anchor="middle" font-family="var(--fd)">N</text>
            <rect x="4" y="3" width="122" height="6" rx="3" fill="#ffffff" opacity="0.35"/>
          </g>

          <!-- Repulsion Deflection Barrier -->
          <g transform="translate(175, 20)">
            <path d="M 40 10 Q 55 48 40 86" stroke="#ef4444" stroke-width="4" fill="none" stroke-linecap="round"/>
            <path d="M 90 10 Q 75 48 90 86" stroke="#ef4444" stroke-width="4" fill="none" stroke-linecap="round"/>
            <text x="65" y="54" font-size="28" text-anchor="middle">🚫</text>
            <text x="65" y="86" font-size="11" font-weight="900" fill="#ef4444" text-anchor="middle" font-family="var(--fd)">PUSH AWAY ⬅️ ➔</text>
          </g>

          <!-- Magnet 2: [N] facing Magnet 1's [N] -->
          <g transform="translate(315, 34)">
            <rect x="3" y="5" width="130" height="48" rx="8" fill="#000000" opacity="0.45"/>
            <!-- North Half (Blue) facing center -->
            <rect x="0" y="0" width="65" height="48" rx="8" fill="url(#magBlue2)" stroke="#0369a1" stroke-width="2"/>
            <text x="32" y="32" font-size="22" font-weight="900" fill="#ffffff" text-anchor="middle" font-family="var(--fd)">N</text>
            <!-- South Half (Red) -->
            <rect x="65" y="0" width="65" height="48" rx="8" fill="url(#magRed2)" stroke="#7f1d1d" stroke-width="2"/>
            <text x="98" y="32" font-size="22" font-weight="900" fill="#ffffff" text-anchor="middle" font-family="var(--fd)">S</text>
            <rect x="4" y="3" width="122" height="6" rx="3" fill="#ffffff" opacity="0.35"/>
          </g>
        </svg>
      </div>
      <div class="disp-pill">🧲 LIKE POLES (NORTH & NORTH) REPEL (PUSH AWAY)</div>
    `,

    // Big Copper Cooking Pan with Melting Chocolate and Steam Curls
    chocolatePan: (isMelted = true) => `
      <div class="disp-spotlight">
        <svg viewBox="0 0 460 135">
          <defs>
            <linearGradient id="panCopper" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#f97316"/>
              <stop offset="40%" stop-color="#c2410c"/>
              <stop offset="100%" stop-color="#7c2d12"/>
            </linearGradient>
            <linearGradient id="chocMelt" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#78350f"/>
              <stop offset="60%" stop-color="#451a03"/>
              <stop offset="100%" stop-color="#271003"/>
            </linearGradient>
          </defs>

          <!-- Cooking Stove Flame Under Pan -->
          <g transform="translate(190, 85)">
            <!-- Outer Orange Flame -->
            <path d="M 0 20 Q 20 -15 20 20 Q 40 -20 40 20 Q 60 -15 60 20 Q 80 -10 80 20 Z" fill="#f97316" opacity="0.85"/>
            <!-- Inner Yellow Core -->
            <path d="M 12 20 Q 25 -5 25 20 Q 40 -10 40 20 Q 55 -5 55 20 Z" fill="#ffd166"/>
            <!-- Blue Hot Core Base -->
            <ellipse cx="40" cy="20" rx="35" ry="6" fill="#38bdf8" opacity="0.9"/>
          </g>

          <!-- Heavy Copper Skillet Pan -->
          <g transform="translate(110, 18)">
            <!-- Pan Long Handle (Right) -->
            <path d="M 180 50 L 260 30" stroke="#78350f" stroke-width="12" stroke-linecap="round"/>
            <path d="M 180 50 L 260 30" stroke="#ffd166" stroke-width="4" stroke-linecap="round" opacity="0.5"/>
            <!-- Outer Copper Skillet Rim -->
            <ellipse cx="110" cy="54" rx="95" ry="34" fill="url(#panCopper)" stroke="#7c2d12" stroke-width="3"/>
            <!-- Inner Cooking Surface -->
            <ellipse cx="110" cy="50" rx="86" ry="28" fill="#1e293b"/>

            ${isMelted ? `
              <!-- Rich Glossy Melted Chocolate Pool -->
              <ellipse cx="110" cy="50" rx="76" ry="22" fill="url(#chocMelt)"/>
              <!-- Melt Highlights & Swirls -->
              <ellipse cx="100" cy="46" rx="55" ry="14" fill="#92400e" opacity="0.75"/>
              <path d="M 65 48 Q 110 38 150 48" stroke="#fef3c7" stroke-width="2.5" fill="none" opacity="0.35" stroke-linecap="round"/>
              <!-- Dissolving Chocolate Chunks -->
              <rect x="70" y="42" width="22" height="12" rx="3" fill="#451a03" stroke="#271003" stroke-width="1.2"/>
              <rect x="125" y="44" width="20" height="10" rx="3" fill="#451a03" stroke="#271003" stroke-width="1.2"/>
              <!-- Rising Steam Curls -->
              <path d="M 80 32 Q 74 18 84 8 Q 94 -2 86 -10" stroke="rgba(255,255,255,0.75)" stroke-width="2.5" fill="none" stroke-linecap="round"/>
              <path d="M 110 28 Q 118 14 110 4 Q 102 -6 112 -12" stroke="rgba(255,255,255,0.75)" stroke-width="3" fill="none" stroke-linecap="round"/>
              <path d="M 140 32 Q 134 18 144 8 Q 154 -2 146 -10" stroke="rgba(255,255,255,0.75)" stroke-width="2.5" fill="none" stroke-linecap="round"/>
              <text x="110" y="98" font-size="12" font-weight="900" fill="#fde047" text-anchor="middle" font-family="var(--fd)">MELTED LIQUID CHOCOLATE 🍫💧</text>
            ` : `
              <!-- Solid Chocolate Bar before melting -->
              <rect x="68" y="36" width="84" height="30" rx="5" fill="#451a03" stroke="#271003" stroke-width="2"/>
              <line x1="96" y1="36" x2="96" y2="66" stroke="#78350f" stroke-width="1.8"/>
              <line x1="124" y1="36" x2="124" y2="66" stroke="#78350f" stroke-width="1.8"/>
              <text x="110" y="98" font-size="12" font-weight="900" fill="#93c5fd" text-anchor="middle" font-family="var(--fd)">SOLID CHOCOLATE BAR 🍫</text>
            `}
          </g>
        </svg>
      </div>
      <div class="disp-pill">🔥 THERMAL ENERGY · HEAT CAUSES MELTING (SOLID ➔ LIQUID)</div>
    `,

    // Frying Egg (Irreversible Change)
    friedEgg: () => `
      <div class="disp-spotlight">
        <svg viewBox="0 0 460 135">
          <g transform="translate(130, 15)">
            <!-- Pan Base -->
            <ellipse cx="100" cy="50" rx="90" ry="32" fill="#334155" stroke="#64748b" stroke-width="2.5"/>
            <!-- Fried Egg White -->
            <path d="M 40 50 Q 55 25 90 28 Q 130 22 155 45 Q 165 72 135 76 Q 80 82 50 68 Z" fill="#ffffff" stroke="#e2e8f0" stroke-width="2"/>
            <!-- Sunny Yolk -->
            <circle cx="100" cy="50" r="18" fill="#fbbf24" stroke="#f59e0b" stroke-width="2"/>
            <circle cx="94" cy="45" r="4.5" fill="#ffffff" opacity="0.7"/>
            <text x="100" y="100" font-size="12" font-weight="900" fill="#fde68a" text-anchor="middle" font-family="var(--fd)">COOKED FRIED EGG 🍳</text>
          </g>
        </svg>
      </div>
      <div class="disp-pill">🍳 COOKING AN EGG · PERMANENT CHEMICAL CHANGE (IRREVERSIBLE)</div>
    `,

    // FIX RAMP EXPERIMENT: Slopes DOWN from HIGH on left to FLOOR on right.
    // The rough towel/rug is laid FLAT ON THE FLOOR AT THE END (bottom) of the ramp!
    rampFriction: (hasRoughTowel = true) => `
      <div class="disp-spotlight">
        <svg viewBox="0 0 480 135">
          <defs>
            <linearGradient id="towelPattern" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#d97706"/>
              <stop offset="25%" stop-color="#b45309"/>
              <stop offset="50%" stop-color="#d97706"/>
              <stop offset="75%" stop-color="#b45309"/>
              <stop offset="100%" stop-color="#d97706"/>
            </linearGradient>
          </defs>

          <!-- Flat Laboratory Floor across the entire base (y=105) -->
          <line x1="20" y1="105" x2="460" y2="105" stroke="#64748b" stroke-width="3.5" stroke-linecap="round"/>

          <!-- High Support Stack on the Left (Books / Lab Block) -->
          <g transform="translate(30, 35)">
            <rect x="0" y="0" width="46" height="70" rx="3" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
            <!-- Book Spine Details -->
            <line x1="0" y1="22" x2="46" y2="22" stroke="#38bdf8" stroke-width="1.8"/>
            <line x1="0" y1="46" x2="46" y2="46" stroke="#38bdf8" stroke-width="1.8"/>
            <text x="23" y="16" font-size="9" font-weight="bold" fill="#ffd166" text-anchor="middle">LAB BOOKS</text>
          </g>

          <!-- Inclined Ramp Board: Slopes DOWN from High Left (x=70, y=35) to Low Floor Right (x=200, y=105) -->
          <polygon points="70,35 200,105 196,108 66,38" fill="#38bdf8" stroke="#0284c7" stroke-width="1.5"/>
          <line x1="70" y1="35" x2="200" y2="105" stroke="#00f5d4" stroke-width="4" stroke-linecap="round"/>
          <text x="110" y="42" font-size="10" font-weight="bold" fill="#ffd166">Incline Slope ↘️</text>

          <!-- Toy Car rolling DOWN the incline towards the right -->
          <g transform="translate(130, 68) rotate(28)">
            <!-- Car Body -->
            <rect x="-18" y="-10" width="36" height="18" rx="5" fill="#ef4444" stroke="#ffffff" stroke-width="1.8"/>
            <rect x="-10" y="-8" width="18" height="9" rx="3" fill="#38bdf8" stroke="#ffffff" stroke-width="1"/>
            <!-- Wheels -->
            <circle cx="-10" cy="10" r="5" fill="#0f172a" stroke="#cbd5e1" stroke-width="1.5"/>
            <circle cx="10" cy="10" r="5" fill="#0f172a" stroke="#cbd5e1" stroke-width="1.5"/>
          </g>
          <text x="145" y="58" font-size="10" font-weight="bold" fill="#00f5d4">Gravity ⬇️</text>

          <!-- Flat Floor Zone at the Bottom of the Ramp (x=200 to x=450) -->
          ${hasRoughTowel ? `
            <!-- Thick Rough Towel / Rug laid FLAT ON THE FLOOR at the end of the ramp -->
            <g transform="translate(210, 94)">
              <!-- Towel Body -->
              <rect x="0" y="0" width="190" height="11" rx="2" fill="url(#towelPattern)" stroke="#78350f" stroke-width="1.5"/>
              <!-- Fringe Threads / Rug Pile Texture -->
              <line x1="0" y1="2" x2="0" y2="9" stroke="#fde68a" stroke-width="2"/>
              <line x1="190" y1="2" x2="190" y2="9" stroke="#fde68a" stroke-width="2"/>
              <!-- Wavy coarse pile texture -->
              <path d="M 10 3 Q 15 1 20 3 Q 25 5 30 3 Q 35 1 40 3 M 60 3 Q 65 1 70 3 Q 75 5 80 3 M 110 3 Q 115 1 120 3 Q 125 5 130 3 M 150 3 Q 155 1 160 3 Q 165 5 170 3" stroke="#fde68a" stroke-width="1.5" fill="none"/>
              <text x="95" y="24" font-size="11" font-weight="900" fill="#f59e0b" text-anchor="middle" font-family="var(--fd)">ROUGH TOWEL ON FLOOR = SLOWS DOWN! 🛑</text>
            </g>
            <!-- Car hitting the towel and slowing down -->
            <g transform="translate(320, 92)">
              <rect x="-14" y="-8" width="28" height="14" rx="4" fill="#ef4444" stroke="#ffffff" stroke-width="1.5"/>
              <circle cx="-8" cy="8" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
              <circle cx="8" cy="8" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
              <!-- Friction sparks -->
              <text x="18" y="2" font-size="12">💥</text>
            </g>
          ` : `
            <!-- Smooth Tile Surface -->
            <g transform="translate(210, 96)">
              <line x1="0" y1="9" x2="220" y2="9" stroke="#38bdf8" stroke-width="4" stroke-linecap="round"/>
              <text x="110" y="24" font-size="11" font-weight="900" fill="#38bdf8" text-anchor="middle" font-family="var(--fd)">SMOOTH TILE FLOOR = FASTER! 💨</text>
            </g>
            <g transform="translate(380, 92)">
              <rect x="-14" y="-8" width="28" height="14" rx="4" fill="#ef4444" stroke="#ffffff" stroke-width="1.5"/>
              <circle cx="-8" cy="8" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
              <circle cx="8" cy="8" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
              <text x="18" y="4" font-size="12">💨</text>
            </g>
          `}
        </svg>
      </div>
      <div class="disp-pill">🚗 FRICTION RUBS AGAINST TIRES ON THE FLOOR AND SLOWS MOTION</div>
    `,

    // Chicken Life Cycle (Exam vs Lab: Exam Mode HIDES names and displays Stage 1 ➔ Stage 2 ➔ Stage 3 ➔ Stage 4)
    chickenCycle4: (isExam = false) => `
      <div class="disp-spotlight">
        <svg viewBox="0 0 480 135">
          <!-- Stage 1: Egg in nest -->
          <g transform="translate(25, 20)">
            <!-- Cozy nest -->
            <ellipse cx="30" cy="56" rx="26" ry="10" fill="#92400e" stroke="#78350f" stroke-width="1.8"/>
            <!-- Glossy Hen Egg -->
            <ellipse cx="30" cy="40" rx="18" ry="24" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
            <ellipse cx="35" cy="34" rx="5" ry="8" fill="#ffffff" opacity="0.6"/>
            <text x="30" y="82" font-size="12" font-weight="900" fill="#fde68a" text-anchor="middle" font-family="var(--fd)">${isExam ? 'Stage 1' : '1. Egg'}</text>
          </g>

          <text x="115" y="60" font-size="20" fill="#ffd166" font-weight="bold" text-anchor="middle">➔</text>

          <!-- Stage 2: Hatchling emerging from shell -->
          <g transform="translate(130, 20)">
            <!-- Cracked egg shell bottom -->
            <path d="M 12 46 Q 30 64 48 46 L 42 38 L 34 44 L 26 38 L 18 44 Z" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
            <!-- Baby chick head with cute beak -->
            <circle cx="30" cy="34" r="14" fill="#fde047" stroke="#eab308" stroke-width="1.8"/>
            <circle cx="26" cy="32" r="2.5" fill="#1e293b"/>
            <polygon points="32,34 38,36 32,38" fill="#f97316"/>
            <!-- Top egg shell on head -->
            <path d="M 20 25 L 26 28 L 30 24 L 36 28 L 40 24 Q 30 14 20 25 Z" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
            <text x="30" y="82" font-size="12" font-weight="900" fill="#fde68a" text-anchor="middle" font-family="var(--fd)">${isExam ? 'Stage 2' : '2. Hatchling'}</text>
          </g>

          <text x="220" y="60" font-size="20" fill="#ffd166" font-weight="bold" text-anchor="middle">➔</text>

          <!-- Stage 3: Fluffy Yellow Chick -->
          <g transform="translate(235, 20)">
            <!-- Chick body -->
            <ellipse cx="30" cy="44" rx="18" ry="16" fill="#fde047" stroke="#eab308" stroke-width="2"/>
            <!-- Chick head -->
            <circle cx="38" cy="30" r="12" fill="#fde047" stroke="#eab308" stroke-width="1.8"/>
            <circle cx="41" cy="28" r="2.2" fill="#1e293b"/>
            <polygon points="46,30 52,32 46,34" fill="#f97316"/>
            <!-- Feet -->
            <line x1="26" y1="58" x2="24" y2="66" stroke="#f97316" stroke-width="2" stroke-linecap="round"/>
            <line x1="34" y1="58" x2="34" y2="66" stroke="#f97316" stroke-width="2" stroke-linecap="round"/>
            <text x="30" y="82" font-size="12" font-weight="900" fill="#fde68a" text-anchor="middle" font-family="var(--fd)">${isExam ? 'Stage 3' : '3. Chick'}</text>
          </g>

          <text x="325" y="60" font-size="20" fill="#ffd166" font-weight="bold" text-anchor="middle">➔</text>

          <!-- Stage 4: Adult Chicken / Hen -->
          <g transform="translate(340, 15)">
            <!-- Chicken body -->
            <ellipse cx="40" cy="46" rx="26" ry="22" fill="#f8fafc" stroke="#475569" stroke-width="2"/>
            <!-- Wing -->
            <path d="M 28 42 Q 44 40 50 54 Q 34 56 28 42 Z" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="1.5"/>
            <!-- Head & Neck -->
            <circle cx="56" cy="28" r="14" fill="#f8fafc" stroke="#475569" stroke-width="2"/>
            <!-- Red Comb & Wattle -->
            <path d="M 50 18 Q 54 8 58 16 Q 62 8 66 18 Z" fill="#ef4444"/>
            <ellipse cx="60" cy="38" rx="3.5" ry="6" fill="#ef4444"/>
            <!-- Beak & Eye -->
            <polygon points="66,28 75,31 66,34" fill="#f59e0b"/>
            <circle cx="58" cy="26" r="2.5" fill="#1e293b"/>
            <!-- Legs -->
            <line x1="34" y1="66" x2="32" y2="76" stroke="#f59e0b" stroke-width="2.5" stroke-linecap="round"/>
            <line x1="44" y1="66" x2="44" y2="76" stroke="#f59e0b" stroke-width="2.5" stroke-linecap="round"/>
            <text x="40" y="87" font-size="12" font-weight="900" fill="#fde68a" text-anchor="middle" font-family="var(--fd)">${isExam ? 'Stage 4' : '4. Chicken'}</text>
          </g>
        </svg>
      </div>
      <div class="disp-pill">${isExam ? '🔬 OBSERVE THE 4 STAGES OF DEVELOPMENT' : '🐓 CHICKEN 4-STAGE LIFE CYCLE'}</div>
    `,

    // Butterfly Metamorphosis (Exam Mode HIDES names: Stage 1 ➔ Stage 2 ➔ Stage 3 ➔ Stage 4)
    butterflyCycle4: (isExam = false) => `
      <div class="disp-spotlight">
        <svg viewBox="0 0 480 135">
          <!-- Stage 1: Leaf with eggs -->
          <g transform="translate(25, 20)">
            <ellipse cx="30" cy="46" rx="26" ry="14" fill="#16a34a" stroke="#15803d" stroke-width="2" transform="rotate(-15 30 46)"/>
            <circle cx="24" cy="42" r="3.5" fill="#fef08a" stroke="#ca8a04" stroke-width="1"/>
            <circle cx="32" cy="45" r="3.5" fill="#fef08a" stroke="#ca8a04" stroke-width="1"/>
            <circle cx="28" cy="49" r="3.5" fill="#fef08a" stroke="#ca8a04" stroke-width="1"/>
            <text x="30" y="82" font-size="12" font-weight="900" fill="#6ee7b7" text-anchor="middle" font-family="var(--fd)">${isExam ? 'Stage 1' : '1. Egg'}</text>
          </g>

          <text x="115" y="60" font-size="20" fill="#ffd166" font-weight="bold" text-anchor="middle">➔</text>

          <!-- Stage 2: Cute Striped Caterpillar -->
          <g transform="translate(130, 20)">
            <!-- Caterpillar segments -->
            <circle cx="16" cy="46" r="10" fill="#22c55e" stroke="#15803d" stroke-width="1.8"/>
            <circle cx="26" cy="44" r="10" fill="#84cc16" stroke="#15803d" stroke-width="1.8"/>
            <circle cx="36" cy="45" r="10" fill="#22c55e" stroke="#15803d" stroke-width="1.8"/>
            <circle cx="46" cy="42" r="11" fill="#84cc16" stroke="#15803d" stroke-width="1.8"/>
            <!-- Happy Face -->
            <circle cx="48" cy="40" r="2" fill="#1e293b"/>
            <!-- Antennae -->
            <line x1="50" y1="34" x2="55" y2="26" stroke="#15803d" stroke-width="1.5" stroke-linecap="round"/>
            <text x="30" y="82" font-size="12" font-weight="900" fill="#6ee7b7" text-anchor="middle" font-family="var(--fd)">${isExam ? 'Stage 2' : '2. Caterpillar'}</text>
          </g>

          <text x="220" y="60" font-size="20" fill="#ffd166" font-weight="bold" text-anchor="middle">➔</text>

          <!-- Stage 3: Hanging Chrysalis / Pupa -->
          <g transform="translate(235, 15)">
            <!-- Twig -->
            <line x1="10" y1="20" x2="50" y2="20" stroke="#78350f" stroke-width="3.5" stroke-linecap="round"/>
            <line x1="30" y1="20" x2="30" y2="28" stroke="#ca8a04" stroke-width="2"/>
            <!-- Chrysalis pod -->
            <path d="M 30 28 Q 44 42 34 62 Q 30 68 26 62 Q 16 42 30 28 Z" fill="#10b981" stroke="#047857" stroke-width="2"/>
            <circle cx="28" cy="40" r="1.8" fill="#ffd166"/>
            <circle cx="32" cy="48" r="1.8" fill="#ffd166"/>
            <text x="30" y="87" font-size="12" font-weight="900" fill="#6ee7b7" text-anchor="middle" font-family="var(--fd)">${isExam ? 'Stage 3' : '3. Pupa'}</text>
          </g>

          <text x="325" y="60" font-size="20" fill="#ffd166" font-weight="bold" text-anchor="middle">➔</text>

          <!-- Stage 4: Majestic Monarch Butterfly -->
          <g transform="translate(340, 15)">
            <!-- Left Wing -->
            <path d="M 32 44 Q 10 18 14 38 Q 8 58 32 48 Z" fill="#f97316" stroke="#c2410c" stroke-width="1.8"/>
            <!-- Right Wing -->
            <path d="M 38 44 Q 60 18 56 38 Q 62 58 38 48 Z" fill="#f97316" stroke="#c2410c" stroke-width="1.8"/>
            <!-- Body -->
            <ellipse cx="35" cy="45" rx="3.5" ry="16" fill="#1e293b"/>
            <!-- Antennae -->
            <path d="M 34 32 Q 28 22 24 24" stroke="#1e293b" stroke-width="1.5" fill="none"/>
            <path d="M 36 32 Q 42 22 46 24" stroke="#1e293b" stroke-width="1.5" fill="none"/>
            <text x="35" y="87" font-size="12" font-weight="900" fill="#f472b6" text-anchor="middle" font-family="var(--fd)">${isExam ? 'Stage 4' : '4. Butterfly'}</text>
          </g>
        </svg>
      </div>
      <div class="disp-pill">${isExam ? '🔬 OBSERVE THE 4 STAGES OF METAMORPHOSIS' : '🦋 BUTTERFLY 4-STAGE METAMORPHOSIS'}</div>
    `,

    // Frog Life Cycle (Exam Mode HIDES names: Stage 1 ➔ Stage 2 ➔ Stage 3 ➔ Stage 4)
    frogCycle4: (isExam = false) => `
      <div class="disp-spotlight">
        <svg viewBox="0 0 480 135">
          <!-- Stage 1: Frog Spawn Eggs -->
          <g transform="translate(25, 20)">
            <ellipse cx="30" cy="46" rx="24" ry="18" fill="rgba(56,189,248,0.2)" stroke="#38bdf8" stroke-width="1.8"/>
            <circle cx="22" cy="42" r="4.5" fill="#f8fafc" stroke="#0284c7" stroke-width="1"/>
            <circle cx="22" cy="42" r="2" fill="#0f172a"/>
            <circle cx="34" cy="40" r="4.5" fill="#f8fafc" stroke="#0284c7" stroke-width="1"/>
            <circle cx="34" cy="40" r="2" fill="#0f172a"/>
            <circle cx="28" cy="50" r="4.5" fill="#f8fafc" stroke="#0284c7" stroke-width="1"/>
            <circle cx="28" cy="50" r="2" fill="#0f172a"/>
            <text x="30" y="82" font-size="12" font-weight="900" fill="#7dd3fc" text-anchor="middle" font-family="var(--fd)">${isExam ? 'Stage 1' : '1. Egg'}</text>
          </g>

          <text x="115" y="60" font-size="20" fill="#ffd166" font-weight="bold" text-anchor="middle">➔</text>

          <!-- Stage 2: Swimming Tadpole with Gills & Tail -->
          <g transform="translate(130, 20)">
            <!-- Tail -->
            <path d="M 28 46 Q 48 38 62 46 Q 48 54 28 46 Z" fill="#38bdf8" opacity="0.6"/>
            <path d="M 22 46 Q 44 42 60 46" stroke="#0284c7" stroke-width="2.5" fill="none"/>
            <!-- Tadpole Head Body -->
            <ellipse cx="20" cy="46" rx="14" ry="11" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
            <circle cx="16" cy="42" r="2.5" fill="#0f172a"/>
            <circle cx="17" cy="41" r="0.8" fill="#ffffff"/>
            <!-- Feathery External Gills -->
            <path d="M 24 38 Q 28 32 32 36 M 24 40 Q 30 38 34 42" stroke="#ef4444" stroke-width="1.8" fill="none"/>
            <text x="35" y="82" font-size="12" font-weight="900" fill="#7dd3fc" text-anchor="middle" font-family="var(--fd)">${isExam ? 'Stage 2' : '2. Tadpole'}</text>
          </g>

          <text x="220" y="60" font-size="20" fill="#ffd166" font-weight="bold" text-anchor="middle">➔</text>

          <!-- Stage 3: Froglet (Growing legs, shrinking tail) -->
          <g transform="translate(235, 20)">
            <!-- Small tail -->
            <path d="M 20 48 Q 12 52 6 54" stroke="#059669" stroke-width="3" fill="none" stroke-linecap="round"/>
            <!-- Froglet body -->
            <ellipse cx="32" cy="44" rx="15" ry="12" fill="#10b981" stroke="#047857" stroke-width="2"/>
            <!-- Hind Leg -->
            <path d="M 24 48 L 18 56 L 24 60" stroke="#047857" stroke-width="2.5" fill="none" stroke-linecap="round"/>
            <!-- Eye -->
            <circle cx="38" cy="36" r="4.5" fill="#10b981" stroke="#047857" stroke-width="1.5"/>
            <circle cx="38" cy="36" r="2" fill="#0f172a"/>
            <text x="30" y="82" font-size="12" font-weight="900" fill="#7dd3fc" text-anchor="middle" font-family="var(--fd)">${isExam ? 'Stage 3' : '3. Froglet'}</text>
          </g>

          <text x="325" y="60" font-size="20" fill="#ffd166" font-weight="bold" text-anchor="middle">➔</text>

          <!-- Stage 4: Adult Green Frog on Lilypad -->
          <g transform="translate(340, 15)">
            <!-- Water lily pad -->
            <ellipse cx="38" cy="62" rx="30" ry="12" fill="#059669" stroke="#047857" stroke-width="2"/>
            <!-- Frog Body -->
            <ellipse cx="38" cy="45" rx="18" ry="14" fill="#22c55e" stroke="#15803d" stroke-width="2"/>
            <!-- Big Cute Bulging Eyes -->
            <circle cx="28" cy="32" r="6" fill="#22c55e" stroke="#15803d" stroke-width="1.8"/>
            <circle cx="28" cy="32" r="3" fill="#0f172a"/>
            <circle cx="29" cy="30.5" r="1" fill="#fff"/>
            <circle cx="48" cy="32" r="6" fill="#22c55e" stroke="#15803d" stroke-width="1.8"/>
            <circle cx="48" cy="32" r="3" fill="#0f172a"/>
            <circle cx="49" cy="30.5" r="1" fill="#fff"/>
            <!-- Broad Smiling Mouth -->
            <path d="M 28 46 Q 38 54 48 46" stroke="#15803d" stroke-width="2" fill="none" stroke-linecap="round"/>
            <text x="38" y="87" font-size="12" font-weight="900" fill="#6ee7b7" text-anchor="middle" font-family="var(--fd)">${isExam ? 'Stage 4' : '4. Adult Frog'}</text>
          </g>
        </svg>
      </div>
      <div class="disp-pill">${isExam ? '🔬 OBSERVE THE 4 AMPHIBIAN LIFE STAGES' : '🐸 FROG 4-STAGE LIFE CYCLE'}</div>
    `
  };

  /* DYNAMIC POOLS FOR PROFESSOR PIP'S 5 DISCOVERY LABS */
  function getLabRound(labIdx, stepIdx){
    if(labIdx === 0){ // Living Needs Lab
      if(stepIdx === 0){
        return {
          prompt: "Pip needs energy to run! Tap the food group that gives energy:",
          audio: "Pip needs energy to run! Which food gives our body energy?",
          disp: SVG.carbsBreadAndRice(),
          choices: sh([
            { text: "🍞 Bread & Rice (Carbohydrate)", correct: true },
            { text: "🥩 Meat & Fish (Protein)", correct: false },
            { text: "🍎 Apple & Orange (Vitamins)", correct: false }
          ]),
          success: "Awesome! Bread and rice provide carbohydrates for physical energy!"
        };
      }else if(stepIdx === 1){
        return {
          prompt: "Pip wants to grow tall and strong! Tap the food for body growth:",
          audio: "Pip wants to grow tall and strong! Which food group helps our body grow?",
          disp: SVG.proteinFoods(),
          choices: sh([
            { text: "🥩 Fish, Eggs & Meat (Protein)", correct: true },
            { text: "🍞 Bread & Rice (Carbohydrate)", correct: false },
            { text: "🍬 Candy & Soda", correct: false }
          ]),
          success: "Super! Proteins like fish, meat, and eggs build strong muscles!"
        };
      }else{
        return {
          prompt: "Pip wants to stay healthy and fight sickness! Tap the food:",
          audio: "Which food group keeps our body healthy and protects us?",
          disp: SVG.vitaminFoods(),
          choices: sh([
            { text: "🍎 Fruits & Vegetables (Vitamins)", correct: true },
            { text: "🍟 French Fries", correct: false },
            { text: "🧊 Ice Cubes", correct: false }
          ]),
          success: "Brilliant! Fruits and vegetables provide vitamins to keep us healthy!"
        };
      }
    }else if(labIdx === 1){ // Safari Diets Diner
      if(stepIdx === 0){
        return {
          prompt: "A cow 🐮 is hungry! What does a cow eat?",
          audio: "A cow is hungry! What does a cow eat?",
          disp: SVG.cowEatingGrass(),
          choices: sh([
            { text: "🌿 Fresh Grass (Herbivore)", correct: true },
            { text: "🥩 Meat", correct: false }
          ]),
          success: "Moo! Cows eat grass. A cow is a Herbivore (plant-eating animal)!"
        };
      }else if(stepIdx === 1){
        return {
          prompt: "A lion 🦁 hunts for lunch! What does a lion eat?",
          audio: "A lion hunts for lunch! What does a lion eat?",
          disp: SVG.lionEatingMeat(),
          choices: sh([
            { text: "🥩 Meat (Carnivore)", correct: true },
            { text: "🌿 Grass & Leaves", correct: false }
          ]),
          success: "Roar! Lions eat meat. A lion is a Carnivore (meat-eating animal)!"
        };
      }else{
        return {
          prompt: "A bear 🐻 eats fish AND berries! What is a bear?",
          audio: "A bear eats fish and berries. What is a bear?",
          disp: `
            <div class="disp-spotlight">
              <svg viewBox="0 0 460 135">
                <circle cx="230" cy="55" r="42" fill="rgba(168,85,247,0.2)" stroke="#a855f7" stroke-width="2.5"/>
                <text x="230" y="68" font-size="46" text-anchor="middle">🐻</text>
              </svg>
            </div>
            <div class="disp-pill">🐻 OMNIVORE · EATS BOTH PLANTS & MEAT</div>
          `,
          choices: sh([
            { text: "Omnivore (Eats plants AND meat)", correct: true },
            { text: "Carnivore (Only meat)", correct: false }
          ]),
          success: "Yum! Bears eat both plants and meat. A bear is an Omnivore!"
        };
      }
    }else if(labIdx === 2){ // Life Cycle Studio (Teaching Mode with names)
      if(stepIdx === 0){
        return {
          prompt: "Step 1: What is the correct 4-stage life cycle of a domestic chicken?",
          audio: "What is the correct four stage life cycle of a chicken?",
          disp: SVG.chickenCycle4(false),
          choices: sh([
            { text: "1. Egg ➔ 2. Hatchling ➔ 3. Chick ➔ 4. Chicken", correct: true },
            { text: "1. Chick ➔ 2. Egg ➔ 3. Chicken ➔ 4. Hatchling", correct: false },
            { text: "1. Chicken ➔ 2. Tadpole ➔ 3. Egg ➔ 4. Chick", correct: false }
          ]),
          success: "Cluck cluck! Hen lays an egg, hatchling emerges, grows into a chick, then an adult chicken!"
        };
      }else if(stepIdx === 1){
        return {
          prompt: "Step 2: What is the correct 4-stage life cycle of a butterfly?",
          audio: "What is the correct life cycle of a butterfly?",
          disp: SVG.butterflyCycle4(false),
          choices: sh([
            { text: "1. Egg ➔ 2. Caterpillar ➔ 3. Pupa ➔ 4. Butterfly", correct: true },
            { text: "1. Egg ➔ 2. Pupa ➔ 3. Caterpillar ➔ 4. Butterfly", correct: false },
            { text: "1. Caterpillar ➔ 2. Egg ➔ 3. Butterfly ➔ 4. Pupa", correct: false }
          ]),
          success: "Splendid! Egg on leaf ➔ caterpillar larva ➔ resting pupa ➔ colorful butterfly!"
        };
      }else{
        return {
          prompt: "Step 3: In a frog's life cycle, what breathes with gills in the water?",
          audio: "In a frog's life cycle, what breathes with gills in water?",
          disp: SVG.frogCycle4(false),
          choices: sh([
            { text: "🐟 Tadpole (with gills & tail)", correct: true },
            { text: "🐸 Adult Frog (with lungs)", correct: false },
            { text: "🥚 Frog Egg", correct: false }
          ]),
          success: "Ribbit! The tadpole swims with a tail and breathes through gills before growing legs!"
        };
      }
    }else if(labIdx === 3){ // Thermal Lab
      if(stepIdx === 0){
        return {
          prompt: "Pip heats a solid chocolate bar in a pan. What happens?",
          audio: "When we add heat to a solid chocolate bar in a pan, what happens?",
          disp: SVG.chocolatePan(true),
          choices: sh([
            { text: "Melts into liquid chocolate 🍫", correct: true },
            { text: "Freezes into hard ice 🧊", correct: false },
            { text: "Grows bigger 🎈", correct: false }
          ]),
          success: "Delicious! Adding heat makes solid chocolate melt into liquid!"
        };
      }else if(stepIdx === 1){
        return {
          prompt: "If we cool liquid water in the freezer, what happens?",
          audio: "If we cool liquid water in the freezer, what happens?",
          disp: `
            <div class="disp-spotlight">
              <svg viewBox="0 0 460 135">
                <text x="140" y="65" font-size="38" text-anchor="middle">💧</text>
                <text x="230" y="65" font-size="28" fill="#38bdf8" text-anchor="middle">➔ ❄️ ➔</text>
                <text x="320" y="65" font-size="38" text-anchor="middle">🧊</text>
              </svg>
            </div>
            <div class="disp-pill">❄️ COOLING CAUSES FREEZING (LIQUID ➔ SOLID)</div>
          `,
          choices: sh([
            { text: "It freezes into solid ice (Reversible) 🧊", correct: true },
            { text: "It turns into fire 🔥", correct: false }
          ]),
          success: "Yes! Water freezes into ice, and ice melts back into water. It is reversible!"
        };
      }else{
        return {
          prompt: "Which change is permanent and cannot be changed back?",
          audio: "Which change is permanent and cannot be changed back?",
          disp: SVG.friedEgg(),
          choices: sh([
            { text: "Frying an egg 🍳", correct: true },
            { text: "Melting ice into water 💧", correct: false },
            { text: "Melting chocolate 🍫", correct: false }
          ]),
          success: "Spot on! Cooking or frying an egg is permanent (irreversible)!"
        };
      }
    }else{ // Forces & Magnets
      if(stepIdx === 0){
        return {
          prompt: "Look at the boy moving a cart forward away from him. What force is this?",
          audio: "Look at the boy moving a cart forward. What force is he using?",
          disp: `
            <div class="disp-spotlight">
              <svg viewBox="0 0 460 135">
                <circle cx="150" cy="60" r="32" fill="rgba(255,255,255,0.18)" stroke="#38bdf8" stroke-width="2.5"/>
                <text x="150" y="70" font-size="36" text-anchor="middle">🛒</text>
                <path d="M 210 60 L 290 60" stroke="#ffd166" stroke-width="5" stroke-linecap="round"/>
                <polygon points="305,60 285,50 285,70" fill="#ffd166"/>
                <text x="250" y="92" font-size="13" font-weight="900" fill="#ffd166" text-anchor="middle" font-family="var(--fd)">FORWARD ➔</text>
              </svg>
            </div>
            <div class="disp-pill">👉 PUSH MOVES AN OBJECT AWAY FROM YOU</div>
          `,
          choices: sh([
            { text: "A Push force 👉", correct: true },
            { text: "A Pull force 👈", correct: false }
          ]),
          success: "Correct! A push moves an object away from your body!"
        };
      }else if(stepIdx === 1){
        return {
          prompt: "Pip puts a rough towel on the floor. Will the toy car move faster or slower?",
          audio: "If Pip puts a rough towel on the floor, will the car move faster or slower?",
          disp: SVG.rampFriction(true),
          choices: sh([
            { text: "SLOWER (Friction rubs wheels) 🛑", correct: true },
            { text: "FASTER 🚀", correct: false }
          ]),
          success: "Well done! The rough towel creates friction that slows the wheels down!"
        };
      }else{
        return {
          prompt: "Opposite poles (North [N] and South [S]) face each other. What do they do?",
          audio: "Opposite poles North and South face each other. Will they attract or repel?",
          disp: SVG.magnetsAttract(),
          choices: sh([
            { text: "ATTRACT (pull together) 🧲💥", correct: true },
            { text: "REPEL (push away) ⬅️➡️", correct: false }
          ]),
          success: "Brilliant! Opposite poles attract! North pulls South together!"
        };
      }
    }
  }

  const LAB_NAMES = [
    "Living Needs Lab 🥗",
    "Safari Diets Diner 🐯",
    "Life Cycle Studio 🦋",
    "The Thermal Lab 🍫",
    "Forces & Magnets Lab 🧲"
  ];

  /* 15 EXAM CHALLENGES (EXACT SCHOOL EXAM COMPLIANCE WITH STAGE 1..4 HIDDEN ANSWERS) */
  function examQs(diff = 1){
    // Cat 0: Living Needs (3 questions)
    const cat0 = [
      {
        cat: "Living Needs 🥗", catIdx: 0,
        prompt: "Which food group gives our body energy? (Bread and Rice)",
        audio: "Which food group gives our body energy? Bread and Rice.",
        html: SVG.carbsBreadAndRice(),
        opts: sh(["Carbohydrate", "Plastic", "Magnet"]),
        ans: "Carbohydrate"
      },
      {
        cat: "Living Needs 🥗", catIdx: 0,
        prompt: "Fish, eggs, and meat help our body grow. They give us ________.",
        audio: "Fish, eggs, and meat help our body grow. They give us what?",
        html: SVG.proteinFoods(),
        opts: sh(["Protein", "Vitamins", "Gravity", "Plastic"]),
        ans: "Protein"
      },
      {
        cat: "Living Needs 🥗", catIdx: 0,
        prompt: "Fruits and vegetables keep us healthy. They give us ________.",
        audio: "Fruits and vegetables keep us healthy. They give us what?",
        html: SVG.vitaminFoods(),
        opts: sh(["Vitamins", "Carbohydrate", "Metal", "Plastic"]),
        ans: "Vitamins"
      }
    ];

    // Cat 1: Animal Diets (3 questions)
    const cat1 = [
      {
        cat: "Animal Diets 🐯", catIdx: 1,
        prompt: "A lion hunts and eats meat. A lion is a ________.",
        audio: "Look at the lion eating meat. A lion is a what?",
        html: SVG.lionEatingMeat(),
        opts: sh(["Meat-eating animal", "Plant-eating animal", "Non-living thing"]),
        ans: "Meat-eating animal"
      },
      {
        cat: "Animal Diets 🐯", catIdx: 1,
        prompt: "A cow eats grass. A cow is a plant-eating animal.",
        audio: "A cow eats grass. A cow is a plant-eating animal. Is this true or false?",
        html: SVG.cowEatingGrass(),
        opts: ["TRUE", "FALSE"],
        ans: "TRUE"
      },
      {
        cat: "Animal Diets 🐯", catIdx: 1,
        prompt: "Which animal eats both plants and meat? (Omnivore)",
        audio: "Which animal eats both plants and meat?",
        html: `
          <div class="disp-spotlight">
            <svg viewBox="0 0 460 135">
              <circle cx="230" cy="55" r="42" fill="rgba(168,85,247,0.2)" stroke="#a855f7" stroke-width="2.5"/>
              <text x="230" y="68" font-size="46" text-anchor="middle">🐻</text>
            </svg>
          </div>
          <div class="disp-pill">🐻 OMNIVORE · EATS BOTH PLANTS & MEAT</div>
        `,
        opts: sh(["Bear", "Cow", "Sheep", "Lion"]),
        ans: "Bear"
      }
    ];

    // Cat 2: Life Cycles (3 questions) — Note: isExam=true hides the stage names!
    const cat2 = [
      {
        cat: "Life Cycles 🦋", catIdx: 2,
        prompt: "What hatches from a butterfly's egg on a leaf?",
        audio: "What hatches from a butterfly's egg?",
        html: SVG.butterflyCycle4(true),
        opts: sh(["Caterpillar", "Tadpole", "Chick", "Frog"]),
        ans: "Caterpillar"
      },
      {
        cat: "Life Cycles 🦋", catIdx: 2,
        prompt: "What breathes with gills and swims in water before growing legs?",
        audio: "What breathes with gills and swims in water before growing legs?",
        html: SVG.frogCycle4(true),
        opts: sh(["Tadpole", "Adult Frog", "Caterpillar", "Chick"]),
        ans: "Tadpole"
      },
      {
        cat: "Life Cycles 🦋", catIdx: 2,
        prompt: "Which is the correct 4-stage life cycle of a chicken?",
        audio: "Which is the correct 4 stage life cycle of a chicken?",
        html: SVG.chickenCycle4(true),
        opts: sh([
          "Egg ➔ Hatchling ➔ Chick ➔ Chicken",
          "Chick ➔ Egg ➔ Chicken ➔ Hatchling",
          "Chicken ➔ Tadpole ➔ Egg ➔ Chick"
        ]),
        ans: "Egg ➔ Hatchling ➔ Chick ➔ Chicken"
      }
    ];

    // Cat 3: Thermal Changes & States (3 questions)
    const cat3 = [
      {
        cat: "The Thermal Lab 🍫", catIdx: 3,
        prompt: "When we add heat to a solid chocolate bar in a pan, it ________.",
        audio: "When we add heat to a solid chocolate bar in a pan, what happens?",
        html: SVG.chocolatePan(true),
        opts: sh(["Melts into liquid", "Freezes into ice", "Grows bigger"]),
        ans: "Melts into liquid"
      },
      {
        cat: "The Thermal Lab 🍫", catIdx: 3,
        prompt: "Water turning into ice when cooled is a permanent change that cannot be undone.",
        audio: "Water turning into ice when cooled is a permanent change that cannot be undone. True or False?",
        html: `
          <div class="disp-spotlight">
            <svg viewBox="0 0 460 135">
              <text x="140" y="65" font-size="38" text-anchor="middle">💧</text>
              <text x="230" y="65" font-size="28" fill="#38bdf8" text-anchor="middle">➔ ❄️ ➔</text>
              <text x="320" y="65" font-size="38" text-anchor="middle">🧊</text>
            </svg>
          </div>
          <div class="disp-pill">💧 FREEZING WATER INTO ICE IS REVERSIBLE</div>
        `,
        opts: ["TRUE", "FALSE"],
        ans: "FALSE"
      },
      {
        cat: "The Thermal Lab 🍫", catIdx: 3,
        prompt: "Which change cannot be changed back to the start? (Irreversible)",
        audio: "Which change cannot be changed back to the start?",
        html: SVG.friedEgg(),
        opts: sh(["Frying an egg", "Melting ice", "Freezing water", "Melting chocolate"]),
        ans: "Frying an egg"
      }
    ];

    // Cat 4: Forces, Friction & Magnets (3 questions)
    const cat4 = [
      {
        cat: "Forces & Magnets 🧲", catIdx: 4,
        prompt: "Look at the boy moving the cart forward. What force is he using?",
        audio: "Look at the boy moving the cart forward. What force is he using?",
        html: `
          <div class="disp-spotlight">
            <svg viewBox="0 0 460 135">
              <circle cx="150" cy="60" r="32" fill="rgba(255,255,255,0.18)" stroke="#38bdf8" stroke-width="2.5"/>
              <text x="150" y="70" font-size="36" text-anchor="middle">🛒</text>
              <path d="M 210 60 L 290 60" stroke="#ffd166" stroke-width="5" stroke-linecap="round"/>
              <polygon points="305,60 285,50 285,70" fill="#ffd166"/>
              <text x="250" y="92" font-size="13" font-weight="900" fill="#ffd166" text-anchor="middle" font-family="var(--fd)">FORWARD ➔</text>
            </svg>
          </div>
          <div class="disp-pill">👉 PUSH MOVES AN OBJECT FORWARD</div>
        `,
        opts: sh(["A Push", "A Pull", "Heat", "Magnetism"]),
        ans: "A Push"
      },
      {
        cat: "Forces & Magnets 🧲", catIdx: 4,
        prompt: "An apple falls down from a tree to the ground because of ________.",
        audio: "An apple falls down from a tree to the ground because of what?",
        html: `
          <div class="disp-spotlight">
            <svg viewBox="0 0 460 135">
              <circle cx="230" cy="45" r="30" fill="rgba(239,68,68,0.2)" stroke="#ef4444" stroke-width="2.5"/>
              <text x="230" y="55" font-size="36" text-anchor="middle">🍎</text>
              <path d="M 230 80 L 230 102" stroke="#ffd166" stroke-width="4" stroke-linecap="round"/>
              <polygon points="230,110 222,96 238,96" fill="#ffd166"/>
            </svg>
          </div>
          <div class="disp-pill">⬇️ GRAVITY PULLS OBJECTS DOWNWARD</div>
        `,
        opts: sh(["Gravity", "Magnet", "Protein", "Friction"]),
        ans: "Gravity"
      },
      {
        cat: "Forces & Magnets 🧲", catIdx: 4,
        prompt: "Opposite poles (North [N] and South [S]) face each other. Will they attract or repel?",
        audio: "Opposite poles North and South face each other. Will they attract or repel?",
        html: SVG.magnetsAttract(),
        opts: sh(["ATTRACT (pull together)", "REPEL (push away)"]),
        ans: "ATTRACT (pull together)"
      }
    ];

    const all = [...cat0, ...cat1, ...cat2, ...cat3, ...cat4];
    return sh(all).map((q, i) => { q.id = i + 1; return q; });
  }

  return {
    LAB_NAMES,
    getLabRound,
    examQs,
    exam: examQs,
    ok: (q, a) => q.ans === a
  };
})();

/* ============================================================ HIGH-DEFINITION WALLPAPER CERTIFICATE */
const ART = {
  draw(id, name, score, catScores){
    const cv = document.getElementById(id); if(!cv) return;
    const W = 1200, H = 848, dpr = window.devicePixelRatio || 1;
    cv.width = W * dpr; cv.height = H * dpr;
    cv.style.width = W + 'px'; cv.style.height = H + 'px';
    const c = cv.getContext('2d'); c.scale(dpr, dpr);

    if(!c.roundRect){
      c.roundRect = function(x, y, w, h, r = 0){
        if(typeof r === 'number') r = [r, r, r, r];
        c.beginPath();
        c.moveTo(x + r[0], y); c.lineTo(x + w - r[1], y); c.quadraticCurveTo(x + w, y, x + w, y + r[1]);
        c.lineTo(x + w, y + h - r[2]); c.quadraticCurveTo(x + w, y + h, x + w - r[2], y + h);
        c.lineTo(x + r[3], y + h); c.quadraticCurveTo(x, y + h, x, y + h - r[3]);
        c.lineTo(x + r[0]); c.quadraticCurveTo(x, y, x + r[0], y); c.closePath();
      };
    }

    let cs = catScores;
    if(!cs || !Array.isArray(cs) || cs.length !== 5){
      cs = [0, 0, 0, 0, 0];
      let rem = Math.min(score, 15);
      for(let i = 0; i < 5; i++){ const take = Math.min(3, rem); cs[i] = take; rem -= take; }
    }

    // 1. Cosmic Aurora & Quantum Science Twilight Backdrop
    const bg = c.createLinearGradient(0, 0, W, H);
    bg.addColorStop(0, '#040916');
    bg.addColorStop(0.25, '#071e3b');
    bg.addColorStop(0.5, '#0a2e46');
    bg.addColorStop(0.78, '#053830');
    bg.addColorStop(1, '#021614');
    c.fillStyle = bg; c.fillRect(0, 0, W, H);

    // Glowing Aurora River
    c.save();
    c.beginPath();
    c.moveTo(-40, H * 0.85);
    c.bezierCurveTo(W * 0.3, H * 0.6, W * 0.7, H * 0.35, W + 40, H * 0.08);
    c.lineWidth = 190;
    const awGrad = c.createLinearGradient(0, H * 0.85, W, H * 0.08);
    awGrad.addColorStop(0, 'rgba(0, 245, 212, 0.22)');
    awGrad.addColorStop(0.4, 'rgba(0, 180, 216, 0.25)');
    awGrad.addColorStop(0.75, 'rgba(168, 85, 247, 0.22)');
    awGrad.addColorStop(1, 'rgba(255, 209, 102, 0.2)');
    c.strokeStyle = awGrad; c.stroke();
    c.restore();

    // Stardust
    for(let i = 0; i < 280; i++){
      const sx = (Math.sin(i * 997.3) * 0.5 + 0.5) * W;
      const sy = (Math.cos(i * 733.1) * 0.5 + 0.5) * H;
      const sr = (i % 7 === 0) ? 2.5 : (i % 3 === 0) ? 1.6 : 0.9;
      const sa = (i % 5 === 0) ? 0.95 : 0.45;
      const sc = (i % 6 === 0) ? '#ffd166' : (i % 4 === 0) ? '#00f5d4' : (i % 5 === 0) ? '#c084fc' : '#ffffff';
      c.fillStyle = sc; c.globalAlpha = sa;
      c.beginPath(); c.arc(sx, sy, sr, 0, Math.PI * 2); c.fill();
    }
    c.globalAlpha = 1.0;

    // Sparkling 8-point stars
    const sp8 = (x, y, r, col) => {
      c.save(); c.translate(x, y); c.fillStyle = col; c.beginPath();
      for(let i = 0; i < 16; i++){
        const rr = i % 2 === 0 ? r : r * 0.32, a = i * Math.PI / 8;
        i === 0 ? c.moveTo(Math.cos(a) * rr, Math.sin(a) * rr) : c.lineTo(Math.cos(a) * rr, Math.sin(a) * rr);
      }
      c.closePath(); c.fill(); c.restore();
    };
    sp8(110, 110, 18, '#ffd166');
    sp8(W - 110, 110, 18, '#00f5d4');
    sp8(140, 380, 15, '#c084fc');
    sp8(W - 140, 380, 15, '#38bdf8');
    sp8(240, 710, 16, '#34d399');
    sp8(W - 240, 700, 16, '#ffd166');

    // Ornate Golden Guilloché Frame
    const FR = 22;
    c.strokeStyle = '#ffd166'; c.lineWidth = 3.5;
    c.beginPath(); c.roundRect(FR, FR, W - FR * 2, H - FR * 2, 20); c.stroke();
    c.strokeStyle = 'rgba(0, 245, 212, 0.55)'; c.lineWidth = 1.8;
    c.beginPath(); c.roundRect(FR + 10, FR + 10, W - FR * 2 - 20, H - FR * 2 - 20, 14); c.stroke();

    // Corner knots
    const drawCorner = (cx, cy) => {
      c.save(); c.translate(cx, cy);
      c.strokeStyle = '#ffd166'; c.lineWidth = 2.2;
      c.beginPath(); c.moveTo(0, -22); c.lineTo(22, 0); c.lineTo(0, 22); c.lineTo(-22, 0); c.closePath(); c.stroke();
      const gg = c.createRadialGradient(0, 0, 0, 0, 0, 10);
      gg.addColorStop(0, '#ffd166'); gg.addColorStop(1, '#f59e0b');
      c.fillStyle = gg; c.beginPath(); c.arc(0, 0, 7.5, 0, Math.PI * 2); c.fill();
      c.strokeStyle = 'rgba(0, 245, 212, 0.65)'; c.lineWidth = 1.6;
      c.beginPath(); c.arc(0, 0, 29, 0, Math.PI * 2); c.stroke();
      c.restore();
    };
    drawCorner(FR + 16, FR + 16); drawCorner(W - FR - 16, FR + 16);
    drawCorner(FR + 16, H - FR - 16); drawCorner(W - FR - 16, H - FR - 16);

    // Professor Pip Einstein Science Crest
    const lx = W / 2, ly = 80;
    c.save();
    c.save(); c.translate(lx, ly);
    c.fillStyle = 'rgba(0, 245, 212, 0.18)';
    for(let i = 0; i < 16; i++){ c.rotate(Math.PI / 8); c.fillRect(-2.5, -52, 5, 104); }
    c.restore();

    // Einstein Hair on Pip
    c.fillStyle = '#f8fafc'; c.strokeStyle = '#cbd5e1'; c.lineWidth = 2;
    c.beginPath();
    c.arc(lx - 20, ly - 22, 16, 0, Math.PI * 2); c.fill(); c.stroke();
    c.beginPath();
    c.arc(lx + 20, ly - 22, 16, 0, Math.PI * 2); c.fill(); c.stroke();
    c.beginPath();
    c.arc(lx, ly - 32, 18, 0, Math.PI * 2); c.fill(); c.stroke();

    // Mane
    const maneGrad = c.createRadialGradient(lx, ly, 10, lx, ly, 44);
    maneGrad.addColorStop(0, '#f59e0b'); maneGrad.addColorStop(0.7, '#d97706'); maneGrad.addColorStop(1, '#b45309');
    c.fillStyle = maneGrad; c.beginPath(); c.arc(lx, ly, 38, 0, Math.PI * 2); c.fill();
    for(let i = 0; i < 12; i++){
      const a = (i * Math.PI) / 6;
      c.beginPath(); c.arc(lx + Math.cos(a) * 33, ly + Math.sin(a) * 33, 10, 0, Math.PI * 2); c.fill();
    }
    // Face
    c.fillStyle = '#fde047'; c.beginPath(); c.arc(lx, ly + 3, 23, 0, Math.PI * 2); c.fill();
    // Scientist Spectacles
    c.fillStyle = 'rgba(0, 245, 212, 0.35)'; c.strokeStyle = '#00f5d4'; c.lineWidth = 2.5;
    c.beginPath(); c.arc(lx - 10, ly + 2, 9, 0, Math.PI * 2); c.fill(); c.stroke();
    c.beginPath(); c.arc(lx + 10, ly + 2, 9, 0, Math.PI * 2); c.fill(); c.stroke();
    c.beginPath(); c.moveTo(lx - 1, ly + 2); c.lineTo(lx + 1, ly + 2); c.stroke();
    // Eyes
    c.fillStyle = '#1e293b'; c.beginPath(); c.arc(lx - 10, ly + 2, 3.5, 0, Math.PI * 2); c.fill();
    c.beginPath(); c.arc(lx + 10, ly + 2, 3.5, 0, Math.PI * 2); c.fill();
    // Smile
    c.strokeStyle = '#1e293b'; c.lineWidth = 2.2; c.lineCap = 'round';
    c.beginPath(); c.arc(lx, ly + 12, 6, 0.1, Math.PI * 0.9); c.stroke();
    c.restore();

    // Academy Title Ribbon
    c.textAlign = 'center';
    c.font = '900 17px Nunito,sans-serif';
    c.fillStyle = '#ffd166';
    c.fillText("✦  PROFESSOR PIP'S EINSTEIN QUANTUM ACADEMY  ✦", W / 2, 155);

    c.font = 'bold 27px Fredoka One,cursive';
    c.fillStyle = '#00f5d4';
    c.shadowColor = 'rgba(0, 245, 212, 0.7)'; c.shadowBlur = 16;
    c.fillText('★  CERTIFICATE OF SCIENTIFIC EXCELLENCE  ★', W / 2, 198);
    c.shadowBlur = 0;

    c.font = 'italic 17px Nunito,sans-serif';
    c.fillStyle = 'rgba(224,242,254,0.92)';
    c.fillText('This highest royal honors certificate is presented with great pride to:', W / 2, 235);

    // Student's Name in 3D Gold Extrusion
    const studentName = (name || 'Safari Scientist').trim();
    c.textAlign = 'center';
    c.font = '900 66px Fredoka One,cursive';
    const nameY = 312;
    c.fillStyle = 'rgba(0,0,0,0.65)'; c.fillText(studentName, W / 2 + 5, nameY + 6);
    c.fillStyle = '#92400e'; c.fillText(studentName, W / 2 + 3, nameY + 3.5);
    const nameGrad = c.createLinearGradient(0, nameY - 48, 0, nameY + 12);
    nameGrad.addColorStop(0, '#ffffff'); nameGrad.addColorStop(0.3, '#fffde7');
    nameGrad.addColorStop(0.7, '#ffd166'); nameGrad.addColorStop(1, '#f59e0b');
    c.fillStyle = nameGrad;
    c.shadowColor = 'rgba(255,209,102,0.85)'; c.shadowBlur = 24;
    c.fillText(studentName, W / 2, nameY);
    c.shadowBlur = 0;

    // Citation
    c.font = '700 17.5px Nunito,sans-serif';
    c.fillStyle = 'rgba(255,255,255,0.94)';
    c.fillText('for mastering the Prathomsuksa 3 Final Safari Science Examination with outstanding skill!', W / 2, 362);

    // Score Capsule
    const tierLabel = score === 15 ? 'Grand Champion Master 👑' : score >= 13 ? 'Royal Distinction ⭐' : score >= 11 ? 'Honors Explorer 🌟' : 'Safari Scout 🧭';
    const scTxt = `🏆 Score: ${score} / 15 Marks   ·   ${tierLabel}`;
    c.font = 'bold 22px Fredoka One,cursive';
    const scTw = c.measureText(scTxt).width;
    const capW = Math.max(scTw + 64, 460);
    const capH = 48;
    const capX = (W - capW) / 2;
    const capY = 394;
    const scGrad = c.createLinearGradient(capX, capY, capX + capW, capY + capH);
    scGrad.addColorStop(0, 'rgba(15,118,110,0.92)'); scGrad.addColorStop(0.5, 'rgba(0,180,216,0.95)'); scGrad.addColorStop(1, 'rgba(15,118,110,0.92)');
    c.fillStyle = scGrad;
    c.beginPath(); c.roundRect(capX, capY, capW, capH, 24); c.fill();
    c.strokeStyle = '#ffd166'; c.lineWidth = 2.2; c.stroke();
    c.fillStyle = '#ffffff'; c.fillText(scTxt, W / 2, capY + 32);

    // Helper: Vector Star
    function drawVectorStar(cx, cy, rOuter, rInner, isFilled){
      c.save(); c.beginPath();
      for(let i = 0; i < 10; i++){
        const r = i % 2 === 0 ? rOuter : rInner;
        const a = (i * Math.PI) / 5 - Math.PI / 2;
        i === 0 ? c.moveTo(cx + Math.cos(a) * r, cy + Math.sin(a) * r) : c.lineTo(cx + Math.cos(a) * r, cy + Math.sin(a) * r);
      }
      c.closePath();
      if(isFilled){
        const sg = c.createRadialGradient(cx, cy - 2, 2, cx, cy, rOuter);
        sg.addColorStop(0, '#ffffff'); sg.addColorStop(0.3, '#fffde7'); sg.addColorStop(0.7, '#ffd166'); sg.addColorStop(1, '#f59e0b');
        c.fillStyle = sg; c.shadowColor = 'rgba(255,209,102,0.85)'; c.shadowBlur = 10; c.fill();
        c.strokeStyle = '#92400e'; c.lineWidth = 1.2; c.stroke();
      }else{
        c.fillStyle = 'rgba(255,255,255,0.08)'; c.fill();
        c.strokeStyle = 'rgba(255,255,255,0.3)'; c.lineWidth = 1.2; c.stroke();
      }
      c.restore();
    }

    // Five Science Realm Medallions with Category Stars
    const realms = [
      { em: '🥗', name: 'Living Needs', col1: '#064e3b', col2: '#10b981', border: '#34d399' },
      { em: '🐯', name: 'Animal Diets', col1: '#78350f', col2: '#f59e0b', border: '#fde047' },
      { em: '🦋', name: 'Life Cycles', col1: '#581c87', col2: '#a855f7', border: '#c084fc' },
      { em: '🍫', name: 'Thermal Lab', col1: '#831843', col2: '#ec4899', border: '#f472b6' },
      { em: '🧲', name: 'Forces & Magnets', col1: '#0369a1', col2: '#0284c7', border: '#38bdf8' }
    ];
    const rW = 194, rH = 80, rGap = 16;
    const rStartX = (W - (realms.length * rW + (realms.length - 1) * rGap)) / 2;
    const rY = 478;

    realms.forEach((realm, idx) => {
      const rx = rStartX + idx * (rW + rGap);
      const cGrad = c.createLinearGradient(rx, rY, rx, rY + rH);
      cGrad.addColorStop(0, realm.col2); cGrad.addColorStop(1, realm.col1);
      c.fillStyle = cGrad; c.beginPath(); c.roundRect(rx, rY, rW, rH, 14); c.fill();
      c.strokeStyle = realm.border; c.lineWidth = 1.8; c.stroke();
      c.font = 'bold 14px Nunito,sans-serif'; c.fillStyle = '#ffffff';
      c.shadowBlur = 5; c.shadowColor = 'rgba(0,0,0,0.6)';
      c.fillText(`${realm.em} ${realm.name}`, rx + rW / 2, rY + 26);
      c.shadowBlur = 0;

      const earned = cs[idx] || 0;
      const starCx = rx + rW / 2; const starCy = rY + 55;
      drawVectorStar(starCx - 32, starCy, 11, 5, earned >= 1);
      drawVectorStar(starCx, starCy, 11, 5, earned >= 2);
      drawVectorStar(starCx + 32, starCy, 11, 5, earned >= 3);
    });

    // Official 32-point Gold Embossed Seal
    const sigX = 88, sigY = 630;
    c.textAlign = 'left';
    c.font = '700 15px Nunito,sans-serif'; c.fillStyle = 'rgba(224,242,254,0.85)';
    c.fillText('Head Science Master & Quantum Examiner:', sigX, sigY);
    c.font = '900 18px Nunito,sans-serif'; c.fillStyle = '#ffd166';
    c.fillText('🦁 Professor Pip & Quantum Guild', sigX, sigY + 36);

    const now = new Date();
    const dt = now.toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' });
    c.font = '700 14px Nunito,sans-serif'; c.fillStyle = 'rgba(224,242,254,0.7)';
    c.fillText(`Conferred on: ${dt}`, sigX, sigY + 62);

    const sealX = W - 140, sealY = 645, sRad = 52;
    c.save();
    c.fillStyle = '#b91c1c';
    c.beginPath(); c.moveTo(sealX - 16, sealY + 20); c.lineTo(sealX - 30, sealY + 85);
    c.lineTo(sealX - 14, sealY + 75); c.lineTo(sealX + 2, sealY + 85); c.lineTo(sealX + 16, sealY + 20); c.fill();
    c.fillStyle = '#dc2626';
    c.beginPath(); c.moveTo(sealX, sealY + 20); c.lineTo(sealX + 26, sealY + 85);
    c.lineTo(sealX + 12, sealY + 75); c.lineTo(sealX - 4, sealY + 85); c.lineTo(sealX - 18, sealY + 20); c.fill();

    c.save(); c.translate(sealX, sealY);
    c.beginPath();
    for(let i = 0; i < 64; i++){
      const r = i % 2 === 0 ? sRad : sRad - 5;
      const a = (i * Math.PI) / 32;
      i === 0 ? c.moveTo(Math.cos(a) * r, Math.sin(a) * r) : c.lineTo(Math.cos(a) * r, Math.sin(a) * r);
    }
    c.closePath();
    const sGrad = c.createRadialGradient(-10, -10, 5, 0, 0, sRad);
    sGrad.addColorStop(0, '#fef08a'); sGrad.addColorStop(0.4, '#ffd166');
    sGrad.addColorStop(0.8, '#d97706'); sGrad.addColorStop(1, '#92400e');
    c.fillStyle = sGrad;
    c.shadowColor = 'rgba(0,0,0,0.45)'; c.shadowBlur = 10; c.fill();
    c.strokeStyle = '#fef08a'; c.lineWidth = 2; c.stroke();
    c.restore();

    c.strokeStyle = '#92400e'; c.lineWidth = 2;
    c.beginPath(); c.arc(sealX, sealY, sRad - 12, 0, Math.PI * 2); c.stroke();
    c.fillStyle = '#78350f'; c.textAlign = 'center';
    c.font = '900 10.5px Nunito,sans-serif';
    c.fillText('OFFICIAL SEAL', sealX, sealY - 10);
    c.font = '900 12px Fredoka One,cursive';
    c.fillText('GRADE 3', sealX, sealY + 5);
    c.font = '900 9.5px Nunito,sans-serif';
    c.fillText('MEP SCIENCE', sealX, sealY + 18);
    c.restore();
  }
};

/* ============================================================ GAME CONTROLLER */
const G = {
  name: localStorage.getItem('ssq_name') || '',
  camps: JSON.parse(localStorage.getItem('ssq_camps') || '[]'),
  stamped: false,
  inExam: false,
  plays: parseInt(localStorage.getItem('ssq_plays') || '1', 10),
  curCampIdx: 0,
  curStepIdx: 0,
  qs: [],
  qi: 0,
  score: 0,
  missed: [],
  catScores: [0, 0, 0, 0, 0],
  cQ: null
};

function flash(emoji){
  const el = document.createElement('div');
  el.textContent = emoji;
  el.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%,-50%) scale(0);font-size:clamp(5rem,15vw,8rem);pointer-events:none;z-index:9999;transition:transform .35s cubic-bezier(.175,.885,.32,1.275),opacity .35s;opacity:1;filter:drop-shadow(0 8px 24px rgba(0,0,0,.5))';
  document.body.appendChild(el);
  requestAnimationFrame(() => {
    el.style.transform = 'translate(-50%,-50%) scale(1.2)';
    setTimeout(() => {
      el.style.opacity = '0';
      el.style.transform = 'translate(-50%,-50%) scale(0.6)';
      setTimeout(() => el.remove(), 350);
    }, 450);
  });
}

function confetti(){
  const cols = ['#00f5d4','#ffd166','#ff70a6','#8b5cf6','#00b4d8','#34d399'];
  for(let i = 0; i < 48; i++){
    const d = document.createElement('div');
    const col = cols[Math.floor(Math.random() * cols.length)];
    const left = Math.random() * 100;
    const dur = 2 + Math.random() * 2;
    d.style.cssText = `position:fixed;top:-20px;left:${left}vw;width:${8 + Math.random() * 8}px;height:${8 + Math.random() * 8}px;background:${col};border-radius:50%;pointer-events:none;z-index:9998;opacity:.95;animation:cfall ${dur}s linear forwards;box-shadow:0 0 8px ${col}`;
    document.body.appendChild(d);
    setTimeout(() => d.remove(), dur * 1000);
  }
}
if(!document.getElementById('cf-anim')){
  const st = document.createElement('style');
  st.id = 'cf-anim';
  st.textContent = '@keyframes cfall{0%{transform:translateY(0) rotate(0)}100%{transform:translateY(105vh) rotate(720deg);opacity:0}}';
  document.head.appendChild(st);
}

function show(id){
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  const sc = document.getElementById(id);
  if(sc) sc.classList.add('active');
}

function updateNameUI(){
  const nm = G.name || 'Young Scientist';
  const el = document.getElementById('disp-name');
  if(el) el.textContent = nm;
}

function submitName(){
  const inp = document.getElementById('nm-input');
  const val = (inp.value || '').trim();
  if(!val){ inp.focus(); return; }
  G.name = val;
  localStorage.setItem('ssq_name', G.name);
  updateNameUI();
  document.getElementById('name-modal').classList.add('hide');
  CA.ok();
}

function changeName(){
  const inp = document.getElementById('nm-input');
  inp.value = G.name;
  document.getElementById('name-modal').classList.remove('hide');
  inp.focus();
}

function refreshPassport(){
  const done = G.camps.length;
  G.stamped = done >= 5;
  const st = document.getElementById('stamp');
  if(st) st.classList.toggle('on', G.stamped);
  const lk = document.getElementById('exam-lock');
  if(lk){
    lk.textContent = G.stamped ? '✅ All Labs Complete — Ready!' : `🔒 Complete all 5 Discovery Labs (${done}/5 done)`;
  }
  for(let i = 0; i < 5; i++){
    const cs = document.getElementById(`cs${i}`);
    if(cs) cs.textContent = G.camps.includes(i) ? '⭐' : '⬜';
  }
}

function goHome(){
  if(G.inExam && !confirm('Safari Science Exam in progress! Do you want to quit?')) return;
  G.inExam = false;
  show('sc-start');
  refreshPassport();
}

function goTrain(){
  show('sc-train');
  document.getElementById('camp-hub').style.display = 'flex';
  document.getElementById('t-prac').classList.remove('visible');
  document.getElementById('t-done').classList.add('hidden');
  refreshPassport();
}

function backCamps(){
  document.getElementById('camp-hub').style.display = 'flex';
  document.getElementById('t-prac').classList.remove('visible');
  document.getElementById('t-done').classList.add('hidden');
  refreshPassport();
}

/* ============================================================ MODE 1: DISCOVERY LAB ENGINE */
function startCamp(idx){
  G.curCampIdx = idx;
  G.curStepIdx = 0;
  document.getElementById('camp-hub').style.display = 'none';
  document.getElementById('t-done').classList.add('hidden');
  document.getElementById('t-prac').classList.add('visible');
  renderLabStep();
}

let curStepData = null;
function renderLabStep(){
  const labName = SE.LAB_NAMES[G.curCampIdx];
  curStepData = SE.getLabRound(G.curCampIdx, G.curStepIdx);

  document.getElementById('t-ctitle').textContent = labName;
  document.getElementById('t-prog').textContent = `Step ${G.curStepIdx + 1} / 3`;
  document.getElementById('lab-badge').textContent = `EXPERIMENT ${G.curStepIdx + 1} · ${labName.toUpperCase()}`;
  document.getElementById('lab-prompt').textContent = curStepData.prompt;
  document.getElementById('lab-disp').innerHTML = curStepData.disp;
  
  const sb = document.getElementById('lab-success');
  sb.style.display = 'none';

  const cb = document.getElementById('lab-choices');
  cb.innerHTML = '';
  cb.style.display = 'flex';

  curStepData.choices.forEach(ch => {
    const b = document.createElement('button');
    b.className = 'lab-choice-btn';
    b.textContent = ch.text;
    b.onclick = () => handleLabChoice(ch, b, curStepData);
    cb.appendChild(b);
  });

  CA.spk(curStepData.audio);
}

function handleLabChoice(choice, btn, step){
  if(choice.correct){
    CA.ok();
    flash('⭐');
    document.getElementById('lab-choices').style.display = 'none';
    const sb = document.getElementById('lab-success');
    document.getElementById('lab-success-txt').textContent = step.success;
    sb.style.display = 'flex';
    CA.spk(step.success);
  }else{
    CA.isp();
    flash('💡');
    btn.style.opacity = '0.4';
    btn.disabled = true;
    CA.spk("Try again! Pip wants to find the right experiment.");
  }
}

function nextCampStep(){
  G.curStepIdx++;
  if(G.curStepIdx < 3){
    renderLabStep();
  }else{
    // Camp complete!
    if(!G.camps.includes(G.curCampIdx)){
      G.camps.push(G.curCampIdx);
      localStorage.setItem('ssq_camps', JSON.stringify(G.camps));
    }
    refreshPassport();
    CA.fan();
    confetti();
    document.getElementById('t-prac').classList.remove('visible');
    const td = document.getElementById('t-done');
    td.classList.remove('hidden');
    document.getElementById('t-done-score').textContent = `You finished all 3 experiments in ${SE.LAB_NAMES[G.curCampIdx]}!`;
    
    // Linear progression button to next lab
    const nextLabBtn = document.getElementById('btn-next-lab');
    if(G.curCampIdx < 4){
      nextLabBtn.style.display = 'inline-flex';
      nextLabBtn.textContent = `Next Lab: ${SE.LAB_NAMES[G.curCampIdx + 1]} ➔`;
    }else{
      nextLabBtn.style.display = 'none';
    }

    const eb = document.getElementById('t-done-exam-btn');
    if(eb) eb.style.display = G.stamped ? 'inline-flex' : 'none';
  }
}

function goNextLab(){
  if(G.curCampIdx < 4){
    startCamp(G.curCampIdx + 1);
  }else{
    backCamps();
  }
}

function tAudio(){
  if(curStepData) CA.spk(curStepData.audio, true);
}

/* ============================================================ MODE 2: EXAM CHALLENGE */
function startExam(){
  if(G.camps.length < 5){
    flash('🔒');
    alert(`Complete all 5 Discovery Labs first! (${G.camps.length}/5 completed)\nHeading to Einstein's Discovery Labs now... 🧪`);
    goTrain();
    return;
  }
  const ac = CA.gac();
  if(ac && ac.state === 'suspended') ac.resume();
  G.inExam = true;

  const diff = Math.min(G.plays || 1, 5);
  G.qs = SE.examQs(diff);
  G.qi = 0;
  G.score = 0;
  G.missed = [];
  G.catScores = [0, 0, 0, 0, 0];

  G.plays = (G.plays || 1) + 1;
  localStorage.setItem('ssq_plays', G.plays.toString());

  show('sc-exam');
  renderEQ();
}

function renderEQ(){
  if(G.qi >= G.qs.length){ finishExam(); return; }
  const q = G.qs[G.qi];
  G.cQ = q;

  document.getElementById('q-lbl').textContent = `Q ${G.qi + 1} / 15`;
  document.getElementById('pfill').style.width = `${(G.qi / 15) * 100}%`;
  document.getElementById('s-lbl').textContent = `⭐ ${G.score}`;
  document.getElementById('zbadge').textContent = q.cat;
  document.getElementById('q-prompt').textContent = q.prompt;
  document.getElementById('q-disp').innerHTML = q.html;

  const ans = document.getElementById('answers');
  ans.innerHTML = '';
  ans.style.gridTemplateColumns = q.opts.length === 2 ? '1fr 1fr' : q.opts.length === 3 ? '1fr 1fr 1fr' : '1fr 1fr';

  q.opts.forEach(opt => {
    const b = document.createElement('button');
    b.className = 'abtn';
    b.textContent = opt;
    b.dataset.v = opt;
    b.onclick = () => handleEQ(opt, b, q);
    ans.appendChild(b);
  });

  CA.spk(q.audio);
}

let eBusy = false;
function handleEQ(sel, btn, q){
  if(eBusy) return;
  eBusy = true;
  const ok = SE.ok(q, sel);
  document.querySelectorAll('#answers .abtn').forEach(b => {
    b.disabled = true;
    if(b.dataset.v === q.ans) b.classList.add('ok');
  });

  if(!ok){
    G.missed.push(G.qi);
    btn.classList.add('no');
    CA.er();
    flash('❌');
  }else{
    G.score++;
    if(typeof q.catIdx === 'number' && q.catIdx >= 0 && q.catIdx < 5){
      G.catScores[q.catIdx]++;
    }
    CA.ok();
    flash('✅');
  }
  setTimeout(() => { eBusy = false; G.qi++; renderEQ(); }, 850);
}

function eAudio(){
  if(G.cQ) CA.spk(G.cQ.audio, true);
}

/* ============================================================ RESULTS & CERTIFICATE */
function finishExam(){
  G.inExam = false;
  show('sc-res');
  const s = G.score;
  document.getElementById('r-score').textContent = `${s} / 15`;
  document.getElementById('r-trophy').textContent = s >= 14 ? '🏆' : s >= 11 ? '🥈' : '🥉';
  const tp = document.getElementById('r-tier');
  const msg = document.getElementById('r-msg');
  const nm = document.getElementById('nearmiss');
  const cs = document.getElementById('certsec');
  const bc = document.getElementById('bronzecard');

  nm.classList.add('hidden');
  cs.classList.add('hidden');
  bc.classList.add('hidden');

  if(s >= 14){
    tp.className = 'tpill tg'; tp.textContent = '👑 GOLD MASTER!';
    msg.textContent = `Incredible, ${G.name}! You are an official Thai Safari Science Champion!`;
    CA.fan(); confetti();
    cs.classList.remove('hidden');
    setTimeout(() => ART.draw('cv-cert', G.name, s, G.catScores), 150);
  }else if(s >= 11){
    tp.className = 'tpill ts'; tp.textContent = '🥈 Silver Ranger!';
    msg.textContent = `Great work, ${G.name}! You missed only ${15 - s} questions! Retry to earn Gold!`;
    nm.classList.remove('hidden');
    document.getElementById('nm-desc').textContent = `You scored ${s} / 15 marks. Retry missed questions now to claim your Gold Lion Crown!`;
    document.getElementById('btn-awaken').onclick = retryMissed;
    setTimeout(() => ART.draw('cv-cert', G.name, s, G.catScores), 150);
  }else{
    tp.className = 'tpill tb'; tp.textContent = '🥉 Keep Practicing!';
    msg.textContent = `Every great scientist learns by doing experiments! Let's train in the Science Labs!`;
    bc.classList.remove('hidden');
  }
}

function retryMissed(){
  if(!G.missed.length){ startExam(); return; }
  G.qs = G.missed.map(idx => G.qs[idx]);
  G.qi = 0; G.missed = [];
  show('sc-exam');
  renderEQ();
}

function toggleSilverCert(showCert){
  document.getElementById('nearmiss').classList.toggle('hidden', showCert);
  document.getElementById('certsec').classList.toggle('hidden', !showCert);
  if(showCert) setTimeout(() => ART.draw('cv-cert', G.name, G.score, G.catScores), 100);
}

function dlCert(){
  const cv = document.getElementById('cv-cert');
  if(!cv) return;
  const a = document.createElement('a');
  a.download = `Safari_Science_Certificate_${(G.name || 'Champion').replace(/\\s+/g, '_')}.png`;
  a.href = cv.toDataURL('image/png');
  a.click();
}

/* ============================================================ SCRATCHPAD */
function openSP(){
  document.getElementById('sp-modal').classList.add('active');
  CA.initSP();
}
function closeSP(){
  document.getElementById('sp-modal').classList.remove('active');
}

/* ============================================================ INITIALIZATION */
window.addEventListener('DOMContentLoaded', () => {
  CA.initSP();
  if(!G.name){
    document.getElementById('name-modal').classList.remove('hide');
  }else{
    updateNameUI();
  }
  refreshPassport();
});
</script>
</body>
</html>'''

def generate():
    html = get_html_content()
    root_path = r'c:\GridLock\The safari Quest\safari_science_quest.html'
    with open(root_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated {root_path} (Size: {os.path.getsize(root_path)} bytes)")

    sci_dir = r'c:\GridLock\The safari Quest\science'
    os.makedirs(sci_dir, exist_ok=True)
    sci_index = os.path.join(sci_dir, 'index.html')
    with open(sci_index, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Mirrored to {sci_index} (Size: {os.path.getsize(sci_index)} bytes)")

if __name__ == '__main__':
    generate()
