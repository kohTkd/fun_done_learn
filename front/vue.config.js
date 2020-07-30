// eslint-disable-next-line @typescript-eslint/no-var-requires
const path = require('path');

module.exports = {
  pages: {
    index: {
      entry: 'src/main.ts',
      title: 'Fun Done Learn online Board'
    }
  },
  transpileDependencies: ['vuetify'],
  devServer: {
    overlay: {
      warning: false,
      error: true
    }
  },
  css: {
    loaderOptions: {
      scss: {
        prependData: '@import "./src/sass/main.scss";'
      }
    }
  },
  configureWebpack: {
    resolve: {
      extensions: ['.ts', '.vue', '.json'],
      alias: {
        '@': path.resolve(__dirname, 'src')
      }
    },
    devtool: 'source-map'
  }
};
