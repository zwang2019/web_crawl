const Crypto = require('crypto-js');

// image to base64 string, string to image


/* -------------------------------------------------------------------------------------*/
// node-js method
var a = 'alice' ;

var b = Buffer.from(a, 'utf-8').toString('base64');
console.log(b);

var c = Buffer.from(b, 'base64').toString('utf-8');
console.log(c);

/* -------------------------------------------------------------------------------------*/
// hand-writen base64

function encode64(input) {
  var keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
  var output = "";
  var chr1, chr2, chr3 = "";
  var enc1, enc2, enc3, enc4 = "";
  var i = 0;
  do {
    chr1 = input.charCodeAt(i++);
    chr2 = input.charCodeAt(i++);
    chr3 = input.charCodeAt(i++);
    enc1 = chr1 >> 2;
    enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
    enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
    enc4 = chr3 & 63;
    if (isNaN(chr2)) {
      enc3 = enc4 = 64;
    } else if (isNaN(chr3)) {
      enc4 = 64;
    }
    output = output + keyStr.charAt(enc1) + keyStr.charAt(enc2) +
      keyStr.charAt(enc3) + keyStr.charAt(enc4);
    chr1 = chr2 = chr3 = "";
    enc1 = enc2 = enc3 = enc4 = "";
  } while (i < input.length);

  return output;
}

pwd = encode64('alice');
console.log('password is ', pwd);

/* -------------------------------------------------------------------------------------*/
// Crypto-js encode and decode

my_text = 'hello'
word_array = Crypto.enc.Utf8.parse(my_text)
console.log(`word_array ${my_text} is: `, word_array)

my_base = Crypto.enc.Base64.stringify(word_array);
console.log(`base64 ${my_text} is `, my_base);

parse_base64 = Crypto.enc.Base64.parse(my_base);
console.log('parse base64 is: ', parse_base64);

original = Crypto.enc.Utf8.stringify(parse_base64);
console.log('original text is: ', original);

