/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class',
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // Dark theme color palette for FaceFusion
        primary: {
          bg: '#0D1117',           // Deep Charcoal - Primary Background
          'bg-secondary': '#161B22', // Dark Slate - Secondary Background
          accent: '#00A3FF',        // Electric Blue - Primary Accent
          'accent-hover': '#4DBFFF', // Light Electric Blue - Hover states
          text: '#E6EDF3',          // Off-White - Primary Text
          'text-secondary': '#8B949E', // Muted Gray - Secondary Text
          success: '#34D399',       // Vibrant Green - Success states
          error: '#F87171',         // Bright Red - Error states
          border: '#30363D'         // Subtle Gray - Borders
        }
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
      animation: {
        'glow': 'glow 2s ease-in-out infinite alternate',
        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'fadeIn': 'fadeIn 0.5s ease-in-out',
        'slideUp': 'slideUp 0.3s ease-out',
      },
      keyframes: {
        glow: {
          '0%': { boxShadow: '0 0 5px #00A3FF, 0 0 10px #00A3FF, 0 0 15px #00A3FF' },
          '100%': { boxShadow: '0 0 10px #00A3FF, 0 0 20px #00A3FF, 0 0 30px #00A3FF' }
        },
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' }
        },
        slideUp: {
          '0%': { transform: 'translateY(10px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' }
        }
      },
      boxShadow: {
        'glow': '0 0 15px rgba(0, 163, 255, 0.3)',
        'glow-lg': '0 0 30px rgba(0, 163, 255, 0.4)',
      }
    },
  },
  plugins: [],
}