// /** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./schoole_managment_system/templates/**/*{html,js}", "./node_modules/flowbite/**/*.js"],
  theme: {

    extend: {
      boxShadow: {
        '3xl': '0px 0px 15px -3px rgba(0,0,0,0.20)',
        '4xl': '0px 0px 15px -5px rgba(0,0,0,0.30)',
        '5xl': '0px 0px 15px -6px rgba(0,0,0,0.40)',
      }
    },
  },
  plugins: [
    require('flowbite/plugin')
  ]
}
