const fs = require('fs');
const JSEncrypt = require('jsencrypt')
/* -------------------------------------------------------------------------------------*/
//RSA

const privateKey = fs.readFileSync('./private.pem', 'utf8');
const publicKey = fs.readFileSync('./public.pem', 'utf8');

var encrypt = new JSEncrypt;

// encrypt with public key
function encryptMessage(message, publicKey){
    encrypt.setPublicKey(publicKey);
    return encrypt.encrypt(message);
}

// decrypt with private key
function  decryptMessage(encryptedMessage, privateKey){
    encrypt.setPrivateKey(privateKey);
    return encrypt.decrypt(encryptedMessage);
}

var data = 'Alice';
var enc_mess = encryptMessage(data, publicKey);
console.log(`Encrypted message is: ${enc_mess}`);

var dec_mess = decryptMessage(enc_mess, privateKey);
console.log(`Decrypted message is: ${dec_mess}`);

