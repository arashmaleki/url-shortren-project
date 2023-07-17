module.exports = {
    apps: [
      {
        name: 'Shortener',
        exec_mode: 'cluster',
        instances: 'max',
        script: './node_modules/nuxt/bin/nuxt.js',
        args: 'start'
      }
    ]
  }
