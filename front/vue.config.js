// eslint-disable-next-line @typescript-eslint/no-var-requires
const path = require('path');

module.exports = {
  transpileDependencies: ['vuetify'],
  configureWebpack: {
    resolve: {
      extensions: ['.ts', '.vue', '.json'],
      alias: {
        '@': path.resolve(__dirname, 'src')
      }
    }
  }
};
