const Crypto = require('crypto-js');

/* -------------------------------------------------------------------------------------*/
// md5
var text = '123456';
md5_array = Crypto.MD5(text);
md5_text = md5_array.toString();


console.log(`md5 text of ${text} is ${md5_text}`);

/* -------------------------------------------------------------------------------------*/
// SHA
// SHA1 -> 40 | SHA256 -> 64 | SHA512 -> 128 | SHA3-512 -> 128 | SHA3-384 -> 94 | SHA-n -> n/4

console.log(`SHA1 of ${text} is ${Crypto.SHA1(text).toString()}`);
console.log(`SHA256 of ${text} is ${Crypto.SHA256(text).toString()}`);
console.log(`SHA512 of ${text} is ${Crypto.SHA512(text).toString()}`);