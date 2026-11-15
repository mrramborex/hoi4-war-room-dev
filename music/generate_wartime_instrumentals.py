#!/usr/bin/env python3
"""TOBS Phase 23C.5 - original WWII-era-inspired instrumental broadcasts.

All melodies, song names, motifs and arrangements below are newly authored for
HOI4 War Room. NO samples, soundfonts, period recordings, copyrighted melodies,
or third-party composition files are used. Pure additive synthesis + numpy.
Songs evoke WWII home-front swing, night-watch waltzes, and convoy marches,
but are NOT authentic historical broadcasts.
"""
from pathlib import Path
import json, wave
import numpy as np

ROOT=Path(__file__).resolve().parent.parent
SR=22050
STEP=60.0/104.0
# Explicitly original melodies and harmonic patterns; MIDI pitches, -1 is rest.
SONGS=[
 {"country":"United States","name":"Home Front Swing","slug":"home-front-swing","bpm":132,"meter":4,"style":"swing",
  "melody":[67,69,72,74,76,74,72,69,67,-1,64,67,69,72,71,67,65,67,69,72,74,72,69,67,64,67,69,67,65,64,62,-1],
  "chords":[[48,52,55,58],[53,57,60,64],[50,53,57,60],[55,59,62,65]],
  "lead":"muted_brass","seed":241},
 {"country":"United Kingdom","name":"Blackout Waltz","slug":"blackout-waltz","bpm":112,"meter":3,"style":"waltz",
  "melody":[69,72,74,76,74,72,71,69,67,69,72,-1,74,76,77,76,72,69,67,65,64,67,69,-1],
  "chords":[[45,48,52,57],[41,45,48,53],[43,47,50,55],[40,43,47,52]],
  "lead":"reed","seed":317},
 {"country":"Canada","name":"Atlantic Convoy","slug":"atlantic-convoy","bpm":116,"meter":4,"style":"march",
  "melody":[62,65,69,69,67,65,64,62,65,69,72,69,67,65,62,-1,64,67,71,72,71,69,67,64,62,64,65,69,67,65,62,-1],
  "chords":[[43,47,50,55],[48,52,55,60],[45,48,52,57],[50,54,57,62]],
  "lead":"brass","seed":411},
 {"country":"Australia","name":"Southern Skies Dance","slug":"southern-skies-dance","bpm":126,"meter":4,"style":"swing",
  "melody":[69,72,76,77,76,72,69,67,65,69,72,74,72,69,65,-1,67,71,74,76,74,71,67,64,65,69,72,69,67,65,62,-1],
  "chords":[[45,49,52,55],[50,53,57,60],[47,50,54,57],[52,56,59,62]],
  "lead":"reed","seed":525},
 {"country":"Poland","name":"Warsaw Lanterns","slug":"warsaw-lanterns","bpm":108,"meter":3,"style":"waltz",
  "melody":[74,72,69,67,69,72,74,76,74,72,69,-1,71,72,74,72,69,67,66,69,71,74,72,-1],
  "chords":[[50,53,57,62],[46,50,53,58],[43,46,50,55],[45,48,52,57]],
  "lead":"reed","seed":633},
 {"country":"Soviet Union","name":"Eastern Front Signal","slug":"eastern-front-signal","bpm":118,"meter":4,"style":"march",
  "melody":[64,67,69,71,72,71,69,67,64,67,71,72,74,72,71,-1,69,72,76,74,72,69,67,64,66,69,71,69,67,64,62,-1],
  "chords":[[40,43,47,52],[45,48,52,57],[43,47,50,55],[47,50,54,59]],
  "lead":"brass","seed":751},
]

def midi(note):
 return 440.0 * (2.0**((note-69)/12.0))

def synth(note, seconds, kind, amp=1.0):
 n=max(2,int(seconds*SR))
 t=np.arange(n,dtype=np.float64)/SR
 freq=midi(note)
 phase=2*np.pi*freq*t
 if kind=="reed":
  osc=np.sin(phase)+.28*np.sin(3*phase)+.13*np.sin(5*phase)
 elif kind=="brass":
  osc=np.sin(phase)+.47*np.sin(2*phase)+.25*np.sin(3*phase)+.11*np.sin(4*phase)
 elif kind=="muted_brass":
  osc=np.sin(phase)+.32*np.sin(2*phase)+.1*np.sin(3*phase)
 elif kind=="bass":
  osc=np.sin(phase)+.16*np.sin(2*phase)
 else:
  osc=np.sin(phase)+.23*np.sin(2*phase)+.11*np.sin(3*phase)
 attack=np.minimum(1.0,t/.021)
 decay=np.exp(-t/(seconds*1.8+.1))
 release=np.minimum(1.0,np.maximum(0,(seconds-t))/.11)
 return (osc*attack*decay*release*amp).astype(np.float32)

def place(buf,note,start,length,kind,amp):
 if note<0:return
 i=int(start*SR)
 if i>=len(buf):return
 audio=synth(note,length,kind,amp)
 end=min(len(buf),i+len(audio))
 if end>i:buf[i:end]+=audio[:end-i]

def render(song):
 beat=60/song["bpm"]
 meter=song["meter"]
 phrase= len(song["melody"])
 bars=64 if meter==4 else 80
 length=bars*meter*beat+2.0
 n=int(length*SR)
 mix=np.zeros(n,dtype=np.float32)
 rng=np.random.default_rng(song["seed"])
 notes=song["melody"]
 bar_chords=song["chords"]
 for bar in range(bars):
  base=bar*meter*beat
  chord=bar_chords[(bar//2)%len(bar_chords)]
  # Piano/guitar-like rhythmic chord stabs and walking bass.
  for b in range(meter):
   now=base+b*beat
   bass=chord[0]-12 if b==0 else (chord[2]-12 if b%2 else chord[1]-12)
   place(mix,bass,now,.43*beat,"bass",.15)
   if meter==3:
    if b>0:
     for voice in chord[1:]:place(mix,voice,now,.26*beat,"piano",.039)
   elif b in (1,3):
    for voice in chord[1:]:place(mix,voice,now,.27*beat,"piano",.046)
  # Thematic lead: note length always leads into the next note for organic phrasing.
  for b in range(meter):
   idx=(bar*meter+b)%phrase
   note=notes[idx]
   if bar>=bars-4 and b==meter-1 and bar%2:note=-1
   if bar%16 in (8,12) and b==0 and note>=0:note+=12
   now=base+b*beat
   if song["style"]=="swing" and b%2:now+=.12*beat
   place(mix,note,now,.83*beat,song["lead"],.19)
  # Original dry snare/brush synthetic noise, no sound samples.
  if bar < bars-1:
   for b in range(meter):
    now=base+b*beat
    if meter==4 and b not in (1,3):continue
    if meter==3 and b==0:continue
    dur=.09 if song["style"]=="march" else .045
    size=int(SR*dur)
    noise=rng.normal(0,1,size).astype(np.float32)
    env=np.exp(-np.arange(size,dtype=np.float32)/(SR*(.016 if song["style"]=="march" else .009)))
    start=int(now*SR)
    end=min(n,start+size)
    mix[start:end]+=noise[:end-start]*env[:end-start]*(.036 if song["style"]=="march" else .018)
 # Short original 2-bar ending, with final resolution.
 end_t=(bars-1)*meter*beat
 for note in bar_chords[0][:]:place(mix,note,end_t,1.2,"piano",.08)
 # Subtle historic-radio bandwidth coloration without third-party impulses.
 mix=np.tanh(mix*1.4)
 mix[:int(.02*SR)]*=np.linspace(0,1,int(.02*SR))
 mix[-int(.25*SR):]*=np.linspace(1,0,int(.25*SR))
 peak=float(np.max(np.abs(mix))) or 1.0
 samples=np.int16(np.clip(mix*(.84/peak),-1,1)*32767)
 return samples,length

def main():
 manifest_file=ROOT/"audio-manifest.json"
 manifest=json.loads(manifest_file.read_text("utf-8"))
 assert manifest["version"]==1
 assert len(SONGS)==6
 # Validate every generated file before manifest changes.
 generated=[]
 for song in SONGS:
  arr,seconds=render(song)
  assert len(arr)>SR*40 and np.max(np.abs(arr))>3000
  name="tobs-original-"+song["slug"]+".wav"
  generated.append((song,name,arr,seconds))
  print(f"GENERATED {song['country']} | {song['name']} | {seconds:.1f}s | {len(arr)} frames",flush=True)
 dest=ROOT/"audio";dest.mkdir(exist_ok=True)
 for song,name,arr,seconds in generated:
  with wave.open(str(dest/name),"wb") as output:
   output.setnchannels(1);output.setsampwidth(2);output.setframerate(SR);output.writeframes(arr.tobytes())
  country=song["country"]
  tracks=manifest.setdefault("stations",{}).setdefault(country,[])
  src="audio/"+name
  if not any(track.get("src")==src for track in tracks):
   tracks.append({"title":song["name"]+" — original WWII-era-inspired instrumental","src":src})
 manifest["notes"]="TOBS live receiver: all historical public-domain tracks retained; added six newly composed WWII-era-inspired instrumental pieces made exclusively for HOI4 War Room. These are original new compositions, not historical recordings or famous WWII songs."
 manifest_file.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n","utf-8")
 print("SUCCESS: six original instrumental broadcasts, including first three minor-power stations",flush=True)

if __name__=="__main__":
 main()
