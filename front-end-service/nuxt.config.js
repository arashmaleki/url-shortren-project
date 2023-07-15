export default {
  head: {
    title: 'front-end-service',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [{
        charset: 'utf-8'
      },
      {
        name: 'viewport',
        content: 'width=device-width, initial-scale=1'
      },
      {
        hid: 'description',
        name: 'description',
        content: ''
      },
      {
        name: 'format-detection',
        content: 'telephone=no'
      }
    ],
    link: [{
      rel: 'icon',
      type: 'image/x-icon',
      href: '/favicon.ico'
    }]
  },

  css: [
    '@/assets/css/global.css',
    '@/assets/css/vue-multiselect.min.css',
  ],

  plugins: [
    '~/plugins/axios',
  ],

  components: true,

  buildModules: [],

  modules: [
    '@nuxtjs/axios',
    '@nuxtjs/auth-next',
    'cookie-universal-nuxt',
    'bootstrap-vue/nuxt',
  ],

  axios: {
    baseURL: process.env.API_SERVER_BASE_URL,
  },

  auth: {
    redirect: {
      login: '/',
      logout: '/login',
      home: '/'
    },
    cookie: {
      options: {
        maxAge: 12 * 24 * 60
      }
    },
    strategies: {
      local: {
        token: {
          property: 'token',
          type: 'Bearer',
          maxAge: 12 * 24 * 60,
        },
        endpoints: {
          login: {
            url: `${process.env.API_SERVER_BASE_URL}/api/users/login`,
            method: 'post'
          },
          user: false,
          logout: false
        },
        autoFetchUser: false,
      }
    }
  },

  build: {},

  module: {
    rules: [{
      test: /\.s[ac]ss$/i,
      use: ['style-loader', 'css-loader', 'sass-loader'],
    }, ],
  },

  publicRuntimeConfig: {
    apiServerBaseUrl: process.env.API_SERVER_BASE_URL
  },

  bootstrapVue: {
    componentPlugins: [],
    components: ['BContainer', 'BFormInput', 'BButton', 'BButtonGroup', 'BTable', 'BImgLazy', 'BForm', 'BFormGroup', 'BRow', 'BCol', 'BOverlay',
      'BFormInput', 'BLink', 'BFormRadioGroup', 'BImg', 'BDropdownForm', 'BDropdownItem', 'BDropdown', 'BFormCheckbox', 'BInputGroup', 'BFormCheckboxGroup',
      'BFormTextarea', 'BFormRadio', 'BAvatar', 'BPagination', 'BDropdownForm', 'BDropdownItem', 'BDropdown', 'BCard', 'BPaginationNav',
    ],
    directives: []
  },

  server: {
    port: 8000,
    host: '0.0.0.0',
    timing: false
  }
}