import React, { useContext } from 'react'
import { useNavigate } from 'react-router-dom'
import data from '../ContextApi'
import Cookies from 'js-cookie'

const Home = () => {
    const {userData,setUserData} = useContext(data)
    const navigate = useNavigate()
    console.log(userData.firstName)

    const logout = ()=>{
        setUserData({})
        Cookies.remove('userInfo');
        navigate('/login');
    }

  return (
    <div className='container container-home'>
        <h1>Home page</h1>
        <h2 className="username-home">Hii 👋 {userData.firstName} {userData.lastName}</h2>
        <button className='btn' onClick={logout}>Logout</button>
    </div>
  )
}

export default Home