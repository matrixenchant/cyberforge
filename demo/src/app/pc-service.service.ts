import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {AuthToken, Cooling, Corpus, CPU, Memory, Motherboard, PowerUnit, RAM, UserPC, VideoCard} from "./models";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class PcServiceService {

  BASE_URL = 'http://127.0.0.1:8000'
  constructor(private client:HttpClient) { }
  login(username:string, password:string):Observable<AuthToken>{
    return this.client.post<AuthToken>(`${this.BASE_URL}/api/login/`, {username, password})
  }
  getListUserPC():Observable<UserPC[]>{
    return this.client.get<UserPC[]>(`${this.BASE_URL}/api/userpc/`)
  }
  getUserPC(id:number):Observable<UserPC>{
    return this.client.get<UserPC>(`${this.BASE_URL}/api/userpc/${id}/`)
  }
  addUserPC(userpc:UserPC){
    return this.client.post<UserPC>(`${this.BASE_URL}/api/userpc/`, userpc)
  }
  updateUserPC(userpc:UserPC, id:number){
    return this.client.put<UserPC>(`${this.BASE_URL}/api/userpc/${id}/`, userpc)
  }
  deleteUserPC(id:number){
    return this.client.delete<any>(`${this.BASE_URL}/api/userpc/${id}/`)
  }
  getListCPU():Observable<CPU[]>{
    return this.client.get<CPU[]>(`${this.BASE_URL}/api/cpu/`)
  }
  getCPU(id:number):Observable<CPU>{
    return this.client.get<CPU>(`${this.BASE_URL}/api/cpu/${id}/`)
  }
  getListVideoCard():Observable<VideoCard[]>{
    return this.client.get<VideoCard[]>(`${this.BASE_URL}/api/videocard/`)
  }
  getVideoCard(id:number):Observable<VideoCard>{
    return this.client.get<VideoCard>(`${this.BASE_URL}/api/videocard/${id}/`)
  }
  getListMotherboard():Observable<Motherboard[]>{
    return this.client.get<Motherboard[]>(`${this.BASE_URL}/api/motherboard/`)
  }
  getMotherboard(id:number):Observable<Motherboard>{
    return this.client.get<Motherboard>(`${this.BASE_URL}/api/motherboard/${id}/`)
  }
  getListRAM():Observable<RAM[]>{
    return this.client.get<RAM[]>(`${this.BASE_URL}/api/ram/`)
  }
  getRAM(id:number):Observable<RAM>{
    return this.client.get<RAM>(`${this.BASE_URL}/api/ram/${id}/`)
  }
  getListMemory():Observable<Memory[]>{
    return this.client.get<Memory[]>(`${this.BASE_URL}/api/memory/`)
  }
  getMemory(id:number):Observable<Memory>{
    return this.client.get<Memory>(`${this.BASE_URL}/api/memory/${id}/`)
  }
  getListCooling():Observable<Cooling[]>{
    return this.client.get<Cooling[]>(`${this.BASE_URL}/api/cooling/`)
  }
  getCooling(id:number):Observable<Cooling>{
    return this.client.get<Cooling>(`${this.BASE_URL}/api/cooling/${id}/`)
  }
  getListCorpus():Observable<Corpus[]>{
    return this.client.get<Corpus[]>(`${this.BASE_URL}/api/corpus/`)
  }
  getCorpus(id:number):Observable<Corpus>{
    return this.client.get<Corpus>(`${this.BASE_URL}/api/corpus/${id}/`)
  }
  getListPowerUnit():Observable<PowerUnit[]>{
    return this.client.get<PowerUnit[]>(`${this.BASE_URL}/api/powerunit/`)
  }
  getPowerUnit(id:number):Observable<PowerUnit>{
    return this.client.get<PowerUnit>(`${this.BASE_URL}/api/powerunit/${id}/`)
  }
}
