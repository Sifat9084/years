
html_code = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Years Calculator</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
  <div class="min-h-screen flex flex-col items-center justify-center p-6 relative overflow-hidden" style="background: linear-gradient(135deg, #e0e7ff 0%, #f3e8ff 50%, #e0f2fe 100%);">
    
    <!-- Butterfly 1: Top Right - Teal/Cyan -->
    <div class="absolute top-4 right-8 w-28 h-28">
      <svg viewBox="0 0 100 100" class="w-full h-full drop-shadow-xl">
        <defs>
          <linearGradient id="wing1a" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#67e8f9"/>
            <stop offset="40%" style="stop-color:#0ea5e9"/>
            <stop offset="100%" style="stop-color:#92400e"/>
          </linearGradient>
          <linearGradient id="wing1b" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#a5f3fc"/>
            <stop offset="100%" style="stop-color:#fbbf24"/>
          </linearGradient>
        </defs>
        <path d="M50 50 Q28 18 8 28 Q3 48 28 53 Q50 58 50 50" fill="url(#wing1a)" opacity="0.95"/>
        <path d="M50 50 Q72 18 92 28 Q97 48 72 53 Q50 58 50 50" fill="url(#wing1a)" opacity="0.95"/>
        <path d="M50 50 Q33 72 18 82 Q23 62 45 55" fill="url(#wing1b)" opacity="0.85"/>
        <path d="M50 50 Q67 72 82 82 Q77 62 55 55" fill="url(#wing1b)" opacity="0.85"/>
        <line x1="50" y1="50" x2="44" y2="22" stroke="#374151" stroke-width="1.5" stroke-linecap="round"/>
        <line x1="50" y1="50" x2="56" y2="22" stroke="#374151" stroke-width="1.5" stroke-linecap="round"/>
        <ellipse cx="50" cy="50" rx="2" ry="6" fill="#1f2937"/>
      </svg>
    </div>

    <!-- Butterfly 2: Upper Left - Purple/Green -->
    <div class="absolute top-24 left-4 w-24 h-24">
      <svg viewBox="0 0 100 100" class="w-full h-full drop-shadow-xl">
        <defs>
          <linearGradient id="wing2a" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#d8b4fe"/>
            <stop offset="50%" style="stop-color:#a855f7"/>
            <stop offset="100%" style="stop-color:#15803d"/>
          </linearGradient>
          <linearGradient id="wing2b" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#f3e8ff"/>
            <stop offset="100%" style="stop-color:#86efac"/>
          </linearGradient>
        </defs>
        <path d="M50 50 Q23 12 3 22 Q-2 42 23 47 Q50 52 50 50" fill="url(#wing2a)" opacity="0.95"/>
        <path d="M50 50 Q77 12 97 22 Q102 42 77 47 Q50 52 50 50" fill="url(#wing2a)" opacity="0.95"/>
        <path d="M50 50 Q28 78 13 88 Q18 68 45 55" fill="url(#wing2b)" opacity="0.8"/>
        <path d="M50 50 Q72 78 87 88 Q82 68 55 55" fill="url(#wing2b)" opacity="0.8"/>
        <line x1="50" y1="50" x2="40" y2="18" stroke="#374151" stroke-width="1.5" stroke-linecap="round"/>
        <line x1="50" y1="50" x2="60" y2="18" stroke="#374151" stroke-width="1.5" stroke-linecap="round"/>
        <ellipse cx="50" cy="50" rx="2" ry="6" fill="#1f2937"/>
      </svg>
    </div>

    <!-- Butterfly 3: Bottom Left - Pink Glow -->
    <div class="absolute bottom-16 left-6 w-20 h-20">
      <svg viewBox="0 0 100 100" class="w-full h-full drop-shadow-xl">
        <defs>
          <radialGradient id="wing3a" cx="50%" cy="50%" r="50%">
            <stop offset="0%" style="stop-color:#fff"/>
            <stop offset="25%" style="stop-color:#f9a8d4"/>
            <stop offset="60%" style="stop-color:#ec4899"/>
            <stop offset="100%" style="stop-color:#be185d"/>
          </radialGradient>
          <radialGradient id="wing3b" cx="50%" cy="50%" r="50%">
            <stop offset="0%" style="stop-color:#fce7f3"/>
            <stop offset="100%" style="stop-color:#db2777"/>
          </radialGradient>
        </defs>
        <path d="M50 50 Q18 8 3 28 Q8 53 33 48 Q50 45 50 50" fill="url(#wing3a)" opacity="0.95"/>
        <path d="M50 50 Q82 8 97 28 Q92 53 67 48 Q50 45 50 50" fill="url(#wing3a)" opacity="0.95"/>
        <path d="M50 50 Q28 82 18 92 Q23 72 45 55" fill="url(#wing3b)" opacity="0.85"/>
        <path d="M50 50 Q72 82 82 92 Q77 72 55 55" fill="url(#wing3b)" opacity="0.85"/>
        <circle cx="50" cy="50" r="4" fill="#fff" filter="blur(2px)"/>
        <circle cx="50" cy="50" r="2" fill="#fce7f3"/>
      </svg>
    </div>

    <!-- Butterfly 4: Bottom Right - Blue Glow -->
    <div class="absolute bottom-12 right-8 w-20 h-20">
      <svg viewBox="0 0 100 100" class="w-full h-full drop-shadow-xl">
        <defs>
          <radialGradient id="wing4a" cx="50%" cy="50%" r="50%">
            <stop offset="0%" style="stop-color:#fff"/>
            <stop offset="25%" style="stop-color:#a5b4fc"/>
            <stop offset="60%" style="stop-color:#6366f1"/>
            <stop offset="100%" style="stop-color:#1e3a8a"/>
          </radialGradient>
          <radialGradient id="wing4b" cx="50%" cy="50%" r="50%">
            <stop offset="0%" style="stop-color:#e0e7ff"/>
            <stop offset="100%" style="stop-color:#4338ca"/>
          </radialGradient>
        </defs>
        <path d="M50 50 Q18 8 3 28 Q8 53 33 48 Q50 45 50 50" fill="url(#wing4a)" opacity="0.95"/>
        <path d="M50 50 Q82 8 97 28 Q92 53 67 48 Q50 45 50 50" fill="url(#wing4a)" opacity="0.95"/>
        <path d="M50 50 Q28 82 18 92 Q23 72 45 55" fill="url(#wing4b)" opacity="0.85"/>
        <path d="M50 50 Q72 82 82 92 Q77 72 55 55" fill="url(#wing4b)" opacity="0.85"/>
        <circle cx="50" cy="50" r="4" fill="#fff" filter="blur(2px)"/>
        <circle cx="50" cy="50" r="2" fill="#e0e7ff"/>
      </svg>
    </div>

    <!-- Title -->
    <h1 class="text-5xl font-black text-center mb-10 tracking-tight z-10" style="color: #1e1b4b; text-shadow: 2px 2px 8px rgba(0,0,0,0.1);">
      YEARS CALCULATOR
    </h1>

    <!-- Previous Date Card -->
    <div class="w-full max-w-md mb-5 relative z-10">
      <div class="bg-black rounded-3xl p-6 shadow-2xl border border-gray-800" style="box-shadow: 0 20px 50px rgba(0,0,0,0.3);">
        <label class="block text-white text-2xl font-bold text-center mb-4 tracking-wide">Previous date</label>
        <div class="flex justify-center">
          <input type="date" id="prevDate" class="bg-gray-900 text-white text-lg px-5 py-3 rounded-2xl border-2 border-gray-700 focus:border-cyan-400 focus:outline-none transition-all text-center w-52 hover:border-gray-600" />
        </div>
      </div>
    </div>

    <!-- Present Date Card -->
    <div class="w-full max-w-md mb-5 relative z-10">
      <div class="bg-black rounded-3xl p-6 shadow-2xl border border-gray-800" style="box-shadow: 0 20px 50px rgba(0,0,0,0.3);">
        <label class="block text-white text-2xl font-bold text-center mb-4 tracking-wide">Present date</label>
        <div class="flex justify-center">
          <input type="date" id="presentDate" class="bg-gray-900 text-white text-lg px-5 py-3 rounded-2xl border-2 border-gray-700 focus:border-cyan-400 focus:outline-none transition-all text-center w-52 hover:border-gray-600" />
        </div>
      </div>
    </div>

    <!-- Calculate Button -->
    <button onclick="calculateDiff()" class="mb-5 px-12 py-3.5 bg-gradient-to-r from-cyan-500 via-blue-500 to-indigo-600 text-white font-bold text-lg rounded-2xl shadow-lg hover:shadow-cyan-500/30 transform hover:scale-105 transition-all duration-200 active:scale-95 z-10 border border-cyan-400/30">
      📅 Calculate
    </button>

    <!-- Result Card -->
    <div class="w-full max-w-md relative z-10">
      <div class="bg-black rounded-3xl p-8 shadow-2xl border border-gray-800 relative overflow-hidden" style="box-shadow: 0 20px 50px rgba(0,0,0,0.3);">
        <!-- Pink glow bottom left -->
        <div class="absolute -bottom-4 -left-4 w-32 h-32 bg-pink-500 rounded-full blur-3xl opacity-50"></div>
        <!-- Blue glow bottom right -->
        <div class="absolute -bottom-4 -right-4 w-32 h-32 bg-blue-600 rounded-full blur-3xl opacity-50"></div>
        
        <h2 class="text-white text-4xl font-black text-center mb-6 tracking-wide relative">Result</h2>
        
        <div id="resultArea" class="text-center space-y-3 relative">
          <div class="text-gray-400 text-sm">Enter dates and click Calculate</div>
        </div>
      </div>
    </div>

    <script>
      const today = new Date().toISOString().split('T')[0];
      document.getElementById('presentDate').value = today;

      function calculateDiff() {
        const prev = document.getElementById('prevDate').value;
        const present = document.getElementById('presentDate').value;
        const resultArea = document.getElementById('resultArea');

        if (!prev || !present) {
          resultArea.innerHTML = '<div class="text-red-400 font-semibold text-lg">Please select both dates 📅</div>';
          return;
        }

        const d1 = new Date(prev);
        const d2 = new Date(present);

        if (d2 < d1) {
          resultArea.innerHTML = '<div class="text-red-400 font-semibold text-lg">Present date must be after previous date!</div>';
          return;
        }

        let years = d2.getFullYear() - d1.getFullYear();
        let months = d2.getMonth() - d1.getMonth();
        let days = d2.getDate() - d1.getDate();

        if (days < 0) {
          months--;
          const prevMonth = new Date(d2.getFullYear(), d2.getMonth(), 0);
          days += prevMonth.getDate();
        }
        if (months < 0) {
          years--;
          months += 12;
        }

        const totalDays = Math.floor((d2 - d1) / (1000 * 60 * 60 * 24));
        const totalMonths = years * 12 + months;

        resultArea.innerHTML = `
          <div class="grid grid-cols-3 gap-3 mb-5">
            <div class="bg-gray-900 rounded-2xl p-4 border border-gray-700 hover:border-cyan-500/50 transition-colors">
              <div class="text-4xl font-black text-cyan-400">${years}</div>
              <div class="text-xs text-gray-400 mt-1 uppercase tracking-wider">Years</div>
            </div>
            <div class="bg-gray-900 rounded-2xl p-4 border border-gray-700 hover:border-pink-500/50 transition-colors">
              <div class="text-4xl font-black text-pink-400">${months}</div>
              <div class="text-xs text-gray-400 mt-1 uppercase tracking-wider">Months</div>
            </div>
            <div class="bg-gray-900 rounded-2xl p-4 border border-gray-700 hover:border-blue-500/50 transition-colors">
              <div class="text-4xl font-black text-blue-400">${days}</div>
              <div class="text-xs text-gray-400 mt-1 uppercase tracking-wider">Days</div>
            </div>
          </div>
          <div class="bg-gray-900/50 rounded-xl p-3 border border-gray-800">
            <div class="text-gray-300 text-sm space-y-1.5">
              <div class="flex justify-between px-2"><span>Total Months:</span><span class="text-white font-bold">${totalMonths}</span></div>
              <div class="flex justify-between px-2"><span>Total Days:</span><span class="text-white font-bold">${totalDays.toLocaleString()}</span></div>
            </div>
          </div>
        `;
      }
    </script>
  </div>
</body>
</html>'''

with open('/mnt/agents/output/years_calculator.html', 'w') as f:
    f.write(html_code)

print("File saved successfully!")
print(f"File size: {len(html_code)} characters")
