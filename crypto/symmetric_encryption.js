const Crypto = require('crypto-js');
/* -------------------------------------------------------------------------------------*/
//DES

var key = Crypto.enc.Utf8.parse('theosophist');
console.log(`word_array key is: `, key);
var iv = Crypto.enc.Utf8.parse('thievish');
console.log(`word_array iv is: `, iv);
var text = Crypto.enc.Utf8.parse('thistle');

des_encrypted = Crypto.DES.encrypt(text, key,
    {
            iv: iv,
            mode: Crypto.mode.CBC,
            padding: Crypto.pad.Pkcs7
        }
    ).toString();

console.log(`DES encrypted text is: ${des_encrypted}`);


/* -------------------------------------------------------------------------------------*/
//AES

aes_encrypted = Crypto.AES.encrypt(text, key,
    {
            iv: iv,
            mode: Crypto.mode.CBC,
            padding: Crypto.pad.Pkcs7
        }
    ).toString();

console.log(`AES encrypted text is: ${aes_encrypted}`);