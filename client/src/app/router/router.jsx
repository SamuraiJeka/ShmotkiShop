import { createBrowserRouter } from "react-router-dom"
import MainPage from "../../pages/mainPage/MainPage.jsx"

export const router = createBrowserRouter(
    [
        {
            path: "/",
            element: <MainPage/>
        }
    ]
)