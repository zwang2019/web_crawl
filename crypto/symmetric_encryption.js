const Crypto = require('crypto-js');
/* -------------------------------------------------------------------------------------*/
//DES

var des_key = Crypto.enc.Utf8.parse('eightbyt');    // DES input 8 Bytes key, every 8 bits has 1 parity bit, so the effective key length is 56 bits
console.log(`word_array DES_key is: `, des_key);
var des_iv = Crypto.enc.Utf8.parse('thievish');     // DES input 8 Bytes IV, equal to block size
console.log(`word_array DES_iv is: `, des_iv);
var text = Crypto.enc.Utf8.parse('thistle');

des_encrypted = Crypto.DES.encrypt(text, des_key,
    {
            iv: des_iv,
            mode: Crypto.mode.CBC,
            padding: Crypto.pad.Pkcs7
        }
    ).toString();

console.log(`DES encrypted text is: ${des_encrypted}`);

/* -------------------------------------------------------------------------------------*/
//AES

var aes_key = Crypto.enc.Utf8.parse('AESrequires16or24or32Byt');    // AES input 16/24/32 Bytes key.
console.log(`word_array key is: `, aes_key);
var aes_iv = Crypto.enc.Utf8.parse('ivshouldbe16byte');     // AES block size is 16 bytes, therefore iv should be 16 bytes
console.log(`word_array iv is: `, aes_iv);

aes_encrypted = Crypto.AES.encrypt(text, aes_key,
    {
            iv: aes_iv,
            mode: Crypto.mode.CBC,
            padding: Crypto.pad.Pkcs7
        }
    ).toString();

console.log(`AES encrypted text is: ${aes_encrypted}`);