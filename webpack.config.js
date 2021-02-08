const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');


module.exports = [
    {
      entry: ['./tellme/static/tellme/feedback/script.js'],
      module: {
        rules: [
            {
                test: /\.tsx?$/,
                use: 'ts-loader',
                exclude: /node_modules/
            }
        ],
      },
      resolve: {
        extensions: ['.tsx', '.ts', '.js'],
      },
      output: {
        filename: 'feedback.js',
        path: path.resolve(__dirname, 'tellme/static/tellme/feedback/dist'),
      },
      optimization: {
        minimize: false
      }
    },
    {
      entry: ['./tellme/static/tellme/feedback/style.js'],
      module: {
        rules: [
            {
                test: /\.s[ac]ss$/i,
                use: [
                    // Creates `style` nodes from JS strings
                    MiniCssExtractPlugin.loader,
                    // Translates CSS into CommonJS
                    'css-loader',
                    // Compiles Sass to CSS
                    'sass-loader'
                ],
            },
        ],
      },
      plugins: [
        new MiniCssExtractPlugin({
            filename: "feedback.css"
        })
      ],
      resolve: {
        extensions: ['.css', '.scss'],
      },
      output: {
        path: path.resolve(__dirname, 'tellme/static/tellme/feedback/dist'),
      },
      optimization: {
        minimize: false
      }
    }
];