const Crypto = require('crypto-js');


var text = '123456'
md5_array = Crypto.MD5(text)
md5_text = md5_array.toString()


console.log(`md5 text of ${text} is ${md5_text}`)