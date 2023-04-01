import axios from "axios";
import { Person } from "./model";

const baseUrl = "" // nie wiem jaki

export function getLeaderBoard(company: string): Person[] {
    const [error, ] = await axios.get().then
}