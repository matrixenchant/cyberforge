import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class PcServiceService {

  BASE_URL = 'http://127.0.0.1:8000'
  constructor(private client:HttpClient) { }
  login(username:string, password:string):Observable<AuthToken>{
    return this.client.post<AuthToken>(`${this.BASE_URL}/users/login/`, {username, password})
  }
  getListUserPC():Observable<Modification[]>{
    return this.client.get<Modification[]>(`${this.BASE_URL}/configurator/modifications/`)
  }
  getUserPC(id:number):Observable<Modification>{
    return this.client.get<Modification>(`${this.BASE_URL}/configurator/modifications/${id}/`)
  }
  addUserPC(modification:Modification){
    return this.client.post<Modification>(`${this.BASE_URL}/configurator/modifications/`, modification)
  }
  updateUserPC(modification:Modification, id:number){
    return this.client.put<Modification>(`${this.BASE_URL}/configurator/modifications/${id}/`, modification)
  }
  deleteUserPC(id:number){
    return this.client.delete<any>(`${this.BASE_URL}/configurator/modifications/${id}/`)
  }
  getListCPU():Observable<CPU[]>{
    return this.client.get<CPU[]>(`${this.BASE_URL}/configurator/processor/`)
  }
  getCPU(id:number):Observable<CPU>{
    return this.client.get<CPU>(`${this.BASE_URL}/configurator/processor/${id}/`)
  }
  getListVideoCard():Observable<GPU[]>{
    return this.client.get<GPU[]>(`${this.BASE_URL}/configurator/graphic_card/`)
  }
  getVideoCard(id:number):Observable<GPU>{
    return this.client.get<GPU>(`${this.BASE_URL}/configurator/graphic_card/${id}/`)
  }
  getListMotherboard():Observable<Motherboard[]>{
    return this.client.get<Motherboard[]>(`${this.BASE_URL}/configurator/motherboard/`)
  }
  getMotherboard(id:number):Observable<Motherboard>{
    return this.client.get<Motherboard>(`${this.BASE_URL}/configurator/motherboard/${id}/`)
  }
  getListRAM():Observable<RAM[]>{
    return this.client.get<RAM[]>(`${this.BASE_URL}/configurator/ram/`)
  }
  getRAM(id:number):Observable<RAM>{
    return this.client.get<RAM>(`${this.BASE_URL}/configurator/ram/${id}/`)
  }
  getListMemory():Observable<Memory[]>{
    return this.client.get<Memory[]>(`${this.BASE_URL}/configurator/memory/`)
  }
  getMemory(id:number):Observable<Memory>{
    return this.client.get<Memory>(`${this.BASE_URL}/configurator/memory/${id}/`)
  }
  getListCooling():Observable<Cooling[]>{
    return this.client.get<Cooling[]>(`${this.BASE_URL}/configurator/cooling/`)
  }
  getCooling(id:number):Observable<Cooling>{
    return this.client.get<Cooling>(`${this.BASE_URL}/configurator/cooling/${id}/`)
  }
  getListCorpus():Observable<Housing[]>{
    return this.client.get<Housing[]>(`${this.BASE_URL}/configurator/housing/`)
  }
  getCorpus(id:number):Observable<Housing>{
    return this.client.get<Housing>(`${this.BASE_URL}/configurator/housing/${id}/`)
  }
  getListPowerUnit():Observable<PowerSupplyUnit[]>{
    return this.client.get<PowerSupplyUnit[]>(`${this.BASE_URL}/configurator/power_supply_unit/`)
  }
  getPowerUnit(id:number):Observable<PowerSupplyUnit>{
    return this.client.get<PowerSupplyUnit>(`${this.BASE_URL}/configurator/power_supply_unit/${id}/`)
  }
}
