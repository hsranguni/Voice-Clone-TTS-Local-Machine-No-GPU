/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import { useState, useRef, useEffect } from 'react';
import { Activity, Play, Upload, Sliders, Volume2, Mic, Settings, Search, History, Download, SkipBack, Pause, SkipForward } from 'lucide-react';

export default function App() {
  const [text, setText] = useState("[joy]Welcome back, commander. The latest data harvest from the neural network is complete.[/joy]\n\n[whisper]Would you like to review the anomalies found in the latent space? It seems there are patterns we haven't seen before...[/whisper]");
  const [intensity, setIntensity] = useState(1.24);
  const [nuance, setNuance] = useState(0.85);
  const [isGenerating, setIsGenerating] = useState(false);
  const [audioProgress, setAudioProgress] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);

  const handleSynthesize = () => {
    setIsGenerating(true);
    setTimeout(() => {
      setIsGenerating(false);
    }, 2000);
  };

  const togglePlay = () => {
    if (isPlaying) {
      setIsPlaying(false);
    } else {
      setIsPlaying(true);
      // Mock progress
      let p = 0;
      const interval = setInterval(() => {
        p += 5;
        if (p > 100) {
          clearInterval(interval);
          setIsPlaying(false);
          setAudioProgress(0);
        } else {
          setAudioProgress(p);
        }
      }, 200);
    }
  };

  return (
    <div className="bg-[#050508] min-h-screen text-gray-200 overflow-hidden font-sans flex flex-col p-6 items-center">
      <div className="w-full max-w-6xl w-full flex flex-col gap-6">
        {/* Header Section */}
        <header className="flex items-center justify-between mb-2 border-b border-white/5 pb-4">
          <div className="flex items-center gap-4">
            <div className="w-10 h-10 bg-cyan-500/20 border border-cyan-400/50 rounded-lg flex items-center justify-center shadow-[0_0_15px_rgba(34,211,238,0.2)]">
              <Activity className="w-6 h-6 text-cyan-400" />
            </div>
            <div>
              <h1 className="text-xl font-bold tracking-tight text-white">CHATTERBOX <span className="text-cyan-400">v2.4</span></h1>
              <p className="text-[10px] uppercase tracking-[0.2em] text-gray-500 font-semibold">Local Neural Text-to-Speech Engine</p>
            </div>
          </div>
          <div className="flex gap-6">
            <div className="text-right">
              <p className="text-[10px] text-gray-500 uppercase font-bold">Compute Device</p>
              <p className="text-xs text-emerald-400">NVIDIA RTX 4090 (CUDA)</p>
            </div>
            <div className="text-right flex flex-col justify-end">
              <p className="text-[10px] text-gray-500 uppercase font-bold">Model Status</p>
              <p className="text-xs text-white italic">Multilingual Loaded (23L)</p>
            </div>
          </div>
        </header>

        <main className="flex-1 grid grid-cols-1 md:grid-cols-12 gap-6">
          {/* Left Pane: Input */}
          <section className="col-span-1 md:col-span-7 flex flex-col gap-4">
            <div className="bg-[#0d0d12] border border-white/10 rounded-2xl p-5 flex-1 flex flex-col relative shadow-inner overflow-hidden min-h-[400px]">
              <div className="flex justify-between items-center mb-4">
                <span className="text-xs font-bold text-gray-400 uppercase tracking-widest">Synthesis Input</span>
                <div className="flex gap-2">
                  <span className="px-2 py-1 bg-cyan-900/30 text-cyan-400 text-[10px] rounded border border-cyan-500/30 font-mono">[joy]</span>
                  <span className="px-2 py-1 bg-purple-900/30 text-purple-400 text-[10px] rounded border border-purple-500/30 font-mono">[whisper]</span>
                  <span className="px-2 py-1 bg-rose-900/30 text-rose-400 text-[10px] rounded border border-rose-500/30 font-mono">[angry]</span>
                </div>
              </div>
              
              <textarea 
                value={text}
                onChange={(e) => setText(e.target.value)}
                maxLength={15000}
                className="flex-1 w-full bg-transparent border-none resize-none focus:outline-none text-lg font-light leading-relaxed text-gray-300 font-serif italic"
                spellCheck="false"
              />

              <div className="mt-4 flex justify-between items-center w-full">
                <span className={`text-[10px] font-mono tracking-widest ${text.length >= 15000 ? 'text-rose-400 font-bold' : text.length > 14000 ? 'text-yellow-500' : 'text-gray-500'}`}>
                  {text.length.toLocaleString()} / 15,000 CHARACTERS
                </span>
                
                <button 
                  onClick={handleSynthesize}
                  className="px-8 py-3 bg-cyan-500 text-black font-bold rounded-full hover:bg-cyan-400 transition-all shadow-[0_0_20px_rgba(6,182,212,0.4)] flex items-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
                  disabled={isGenerating || text.length === 0}
                >
                  {isGenerating ? (
                    <div className="w-4 h-4 rounded-full border-2 border-black border-t-transparent animate-spin" />
                  ) : (
                    <Play className="w-4 h-4 fill-current" />
                  )}
                  {isGenerating ? 'SYNTHESIZING...' : 'SYNTHESIZE'}
                </button>
              </div>
            </div>
          </section>

          {/* Right Pane: Controls */}
          <section className="col-span-1 md:col-span-5 flex flex-col gap-4">
            {/* Voice Cloning Card */}
            <div className="bg-[#0d0d12] border border-white/10 rounded-2xl p-5 shadow-lg">
              <h3 className="text-xs font-bold text-gray-400 uppercase mb-4 tracking-widest flex items-center gap-2">
                <Volume2 className="w-4 h-4" />
                Voice Profile / Cloning
              </h3>
              <div className="flex items-center gap-4 mb-4 bg-black/40 p-3 rounded-xl border border-dashed border-white/10 hover:border-cyan-500/30 transition-colors cursor-pointer group">
                <div className="w-12 h-12 bg-white/5 group-hover:bg-cyan-500/10 rounded-lg flex items-center justify-center transition-colors">
                  <Mic className="w-5 h-5 text-gray-500 group-hover:text-cyan-400 transition-colors" />
                </div>
                <div>
                  <p className="text-xs text-white font-medium">Reference: aria_studio.wav</p>
                  <p className="text-[10px] text-gray-500">Duration: 12.4s | Quality: Studio</p>
                </div>
              </div>
              <div className="flex flex-wrap gap-2">
                <span className="px-3 py-1 bg-white/5 border border-white/10 rounded-full text-[10px] text-white">Female</span>
                <span className="px-3 py-1 bg-white/5 border border-white/10 rounded-full text-[10px] text-white">Warm</span>
                <span className="px-3 py-1 bg-white/5 border border-white/10 rounded-full text-[10px] text-white">Mid-Range</span>
              </div>
            </div>

            {/* Parameters Card */}
            <div className="bg-[#0d0d12] border border-white/10 rounded-2xl p-5 flex-1 shadow-lg">
              <h3 className="text-xs font-bold text-gray-400 uppercase mb-6 tracking-widest flex items-center gap-2">
                <Settings className="w-4 h-4" />
                Emotion Exaggeration Controls
              </h3>
              <div className="space-y-6">
                <div>
                  <div className="flex justify-between text-[10px] mb-2 uppercase tracking-wider text-gray-400">
                    <span>Intensity</span>
                    <span className="text-cyan-400">{(intensity).toFixed(2)}x</span>
                  </div>
                  <input
                    type="range"
                    min="0.1"
                    max="2.0"
                    step="0.01"
                    value={intensity}
                    onChange={(e) => setIntensity(parseFloat(e.target.value))}
                    className="w-full accent-cyan-500 bg-white/5 h-1.5 rounded-full outline-none appearance-none cursor-pointer"
                    style={{
                      background: `linear-gradient(to right, #06b6d4 ${(intensity - 0.1) / 1.9 * 100}%, rgba(255,255,255,0.05) ${(intensity - 0.1) / 1.9 * 100}%)`
                    }}
                  />
                </div>
                <div>
                  <div className="flex justify-between text-[10px] mb-2 uppercase tracking-wider text-gray-400">
                    <span>Nuance Factor</span>
                    <span className="text-cyan-400">{(nuance).toFixed(2)}x</span>
                  </div>
                  <input
                    type="range"
                    min="0.1"
                    max="2.0"
                    step="0.01"
                    value={nuance}
                    onChange={(e) => setNuance(parseFloat(e.target.value))}
                    className="w-full accent-cyan-500 bg-white/5 h-1.5 rounded-full outline-none appearance-none cursor-pointer"
                    style={{
                      background: `linear-gradient(to right, #06b6d4 ${(nuance - 0.1) / 1.9 * 100}%, rgba(255,255,255,0.05) ${(nuance - 0.1) / 1.9 * 100}%)`
                    }}
                  />
                </div>
                <div>
                  <div className="flex justify-between text-[10px] mb-2 uppercase tracking-wider text-gray-400">
                    <span>Clarity Tuning</span>
                    <span className="text-cyan-400">High</span>
                  </div>
                  <div className="h-1.5 w-full bg-white/5 rounded-full overflow-hidden">
                    <div className="h-full w-[90%] bg-cyan-500 shadow-[0_0_10px_rgba(6,182,212,0.5)]"></div>
                  </div>
                </div>
              </div>
            </div>
          </section>
        </main>

        {/* Bottom Bar: Playback & History */}
        <footer className="bg-[#0d0d12]/50 border border-white/10 rounded-2xl p-4 flex flex-col md:flex-row md:items-center gap-6 mt-2">
          <div className="flex-1 flex items-center gap-4">
            <button 
              onClick={togglePlay}
              className="w-10 h-10 min-w-10 bg-white/10 rounded-full flex items-center justify-center text-white hover:bg-white/20 transition-colors"
            >
              {isPlaying ? <Pause className="w-5 h-5 fill-current" /> : <Play className="w-5 h-5 fill-current" />}
            </button>
            <div className="flex-1 h-8 flex items-end gap-[2px] relative cursor-pointer group">
              {/* Animated Progress Bar */}
              <div 
                className="absolute top-0 bottom-0 left-0 bg-white/5 rounded pointer-events-none transition-all group-hover:bg-white/10" 
                style={{ width: `${audioProgress}%` }}
              />
              {/* Static Waveform Mockup */}
              <div className="w-full h-full flex items-center gap-1 opacity-60 px-2 justify-between">
                {[12,24,36,18,30,48,24,12,30,42,24,12,18,30,12,6,18,24,40,24,15,8,12,18,32,15,40,48,24,15,10,25].map((h, i) => (
                  <div 
                    key={i} 
                    className={`w-1 rounded-full flex-1 max-w-[4px] ${i < audioProgress / 3 ? 'bg-cyan-400 shadow-[0_0_8px_rgba(34,211,238,0.5)]' : 'bg-gray-600'}`} 
                    style={{ height: `${h}%` }}
                  />
                ))}
              </div>
            </div>
            <span className="text-[10px] font-mono text-gray-500 whitespace-nowrap">
              00:0{Math.floor((audioProgress / 100) * 15 || 4)} / 00:15
            </span>
          </div>
          <div className="flex items-center gap-4 justify-between md:justify-end">
             <div className="hidden md:block border-l border-white/10 h-8"></div>
             <div className="flex gap-2 items-center">
               <History className="w-3 h-3 text-gray-500" />
               <span className="text-[10px] uppercase tracking-widest font-bold text-gray-500">History</span>
               <div className="flex gap-1 ml-2">
                  <div className="w-6 h-6 rounded bg-cyan-900/30 border border-cyan-500/30"></div>
                  <div className="w-6 h-6 rounded bg-white/5 border border-white/10"></div>
                  <div className="w-6 h-6 rounded bg-white/5 border border-white/10"></div>
               </div>
             </div>
             <button className="px-4 py-2 border border-white/10 rounded-lg text-[10px] uppercase font-bold text-gray-400 hover:bg-white/5 hover:text-white transition-colors flex items-center gap-2">
               <Download className="w-3 h-3" />
               Export MP3
             </button>
          </div>
        </footer>
      </div>
    </div>
  );
}
