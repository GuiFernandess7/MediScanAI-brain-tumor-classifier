<template>
    <img class="logo" src="../assets/MediscanCor.png" alt="">
    <h1>Sign up</h1>
    <div class="register">
        <input type="text" placeholder="Enter Full Name" />
        <input crm="text" placeholder="Enter CRM" />
        <input crm="text" placeholder="Enter Email" />
        <input crm="password" placeholder="Enter Password" />
        <button>Sign Up</button>
    </div>
</template>

<script>
export default {
    name: 'SignUp'
}
</script>

<style>
.logo {
    width: 105px;
}
.register input {
    width: 300px;
    height: 40px;
    padding-left: 20px;
    display: block;
    margin-bottom: 30px;
    margin-right: auto;
    margin-left: auto;
    border: 1px solid skyblue;
}

.register button {
    width: 320px;
    height: 40px;
    border: 1px solid skyblue;
    background: skyblue;
    color: #fff;
    cursor: pointer;
}
</style>
