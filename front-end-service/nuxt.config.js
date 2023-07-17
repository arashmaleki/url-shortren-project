export default {
  head: {
    title: 'URL Shortener',
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

  axios: {
    baseURL: process.env.API_SERVER_BASE_URL,
    headers: {
      'X-CSRFToken': 'csrftoken',
    },
    xsrfCookieName: 'csrftoken',
    xsrfHeaderName: 'X-CSRFToken',
  },

  auth: {
    redirect: {
      login: '/home',
      logout: '/login',
      home: '/home'
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
          type: 'Token',
          name: 'Authorization',
          maxAge: 12 * 24 * 60,
        },
        endpoints: {
          login: {
            url: `${process.env.API_SERVER_BASE_URL}/api/user/login/`,
            method: 'post'
          },
          user: false,
          logout: false
        },
        autoFetchUser: false,
      }
    }
  },

  modules: [
    '@nuxtjs/axios',
    '@nuxtjs/auth-next',
    'cookie-universal-nuxt',
    'bootstrap-vue/nuxt',
  ],

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
    components: ['BContainer', 'BFormInput', 'BButton', 'BButtonGroup', 'BTable', 'BImgLazy', 'BForm', 'BFormGroup', 'BRow', 'BCol', 'BOverlay', 'BNavbar', 'BNavbarBrand', 'BNavItem',
      'BFormInput', 'BLink', 'BFormRadioGroup', 'BImg', 'BDropdownForm', 'BDropdownItem', 'BDropdown', 'BFormCheckbox', 'BInputGroup', 'BFormCheckboxGroup', 'BNavbarToggle',
      'BFormTextarea', 'BFormRadio', 'BAvatar', 'BPagination', 'BDropdownForm', 'BDropdownItem', 'BDropdown', 'BCard', 'BPaginationNav', 'BNavItemDropdown', 'BNavbarNav', 'BCollapse',
    ],
    directives: []
  },

  server: {
    port: process.env.NUXT_SERVER_PORT_NUMBER,
    host: process.env.NUXT_SERVER_HOST_ADDRESS,
    timing: false
  }
}
