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

/* -------------------------------------------------------------------------------------*/
// RSA node-forge library

const forge = require('node-forge');

// encrypt with public key
function forgeencrypt(message, publicKey){
    publicKey = forge.pki.publicKeyFromPem(publicKey);
    var encrypted = publicKey.encrypt(message, 'RSA-OAEP');
    return forge.util.encode64(encrypted);    // using forge library have to manually encode with base64
}

// decrypt with private key
function forgeDecrypt(encryptedMessage, privateKey){
    privateKey = forge.pki.privateKeyFromPem(privateKey);
    var encryptedBytes = forge.util.decode64(encryptedMessage);  // using forge library have to manually decode with base64
    return privateKey.decrypt(encryptedBytes, 'RSA-OAEP');
}

var forge_enc_mess = forgeencrypt(data, publicKey);
console.log(`Encrypted message is: ${forge_enc_mess}`);

var forge_dec_mess = forgeDecrypt(forge_enc_mess, privateKey);
console.log(`Decrypted message is: ${forge_dec_mess}`);

/* -------------------------------------------------------------------------------------*/
