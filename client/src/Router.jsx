import { BrowserRouter, Routes, Route } from 'react-router-dom'
import React from 'react'
import LoginPage from "./components/LoginPage"
import Form from "./components/Form"
import NotFound from "./components/NotFound"
import "./css/styles.css"

const Router = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Form />}/>
        <Route path="/login" element={<LoginPage />}/>
        <Route path="*" element={<NotFound />}/>
      </Routes>
    </BrowserRouter>
  )
}

export default Router