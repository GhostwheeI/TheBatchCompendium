/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        // Win95 Flat Minimal Theme Colors
        'win95': {
          white: '#FFFFFF',
          'light-gray': '#E5E5E5',
          'medium-gray': '#C0C0C0',
          'dark-gray': '#7A7A7A',
          black: '#000000',
          blue: '#000080',
          green: '#00AA00',
          red: '#CC0000',
          yellow: '#E0C000',
        },
        // Legacy compatibility
        primary: '#000080',
        secondary: '#C0C0C0',
        success: '#00AA00',
        warning: '#E0C000',
        danger: '#CC0000',
      },
      fontFamily: {
        'win95': ['MS Sans Serif', 'Tahoma', 'Arial', 'sans-serif'],
      },
      fontSize: {
        'win95': '11px',
      },
      borderRadius: {
        'win95': '0px', // Flat - no radius
      },
      boxShadow: {
        'win95': 'none', // Flat - no shadows
      },
    },
  },
  plugins: [],
}
