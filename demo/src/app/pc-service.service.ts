import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class PcServiceService {
  BASE_URL = "http://127.0.0.1:8000"
  constructor(private client:HttpClient) {}
  load:boolean = false;
  getListModification():Observable<Pagination>{
    this.load = true;
    return this.client.get<Pagination>(`${this.BASE_URL}/configurator/modifications/`)
  }
  getListPCComponent(type:string):Observable<Pagination>{
    this.load = true;
    return this.client.get<Pagination>(`${this.BASE_URL}/configurator/${type}/`)
  }
  getNewPage(url:string):Observable<Pagination>{
    this.load = true;
    return this.client.get<Pagination>(url)
  }
  getModification(id:number):Observable<Modification>{
    this.load = true;
    return this.client.get<Modification>(`${this.BASE_URL}/configurator/modifications/${id}/`)
  }
  getComponent(id:number, type:string):Observable<PCComponent>{
    this.load = true;
    return this.client.get<PCComponent>(`${this.BASE_URL}/configurator/${type}/${id}/`)
  }
  checkList(modification:Modification){
    let housing, motherboard, power_supply, cpu, gpu, ram, memory, cooling;
    for(let x of modification.components){
      switch (x.type){
        case "Housing":
          housing = x.id;
          break;
        case "Motherboard":
          motherboard = x.id;
          break;
        case "PowerSupplyUnit":
          power_supply = x.id;
          break;
        case "CPU":
          cpu = x.id;
          break;
        case "GPU":
          gpu = x.id;
          break;
        case "RAM":
          ram = x.id;
          break;
        case "Memory":
          memory = x.id;
          break;
        case "Cooling":
          cooling = x.id;
      }
    }
    return [housing, motherboard, power_supply, cpu, gpu, ram, memory, cooling]
  }
  addModification(modification:Modification):Observable<Modification>{
    let list = this.checkList(modification);
    return this.client.post<Modification>(`${this.BASE_URL}/configurator/modifications/`, {
      name: modification.name, description: modification.description, author_name: modification.author_name,
      likes: modification.likes, housing: list[0], motherboard: list[1], power_supply: list[2],
      cpu: list[3], gpu: list[4], ram: list[5], memory: list[6], cooling: list[7]})
  }
  updateModification(modification:Modification):Observable<Modification>{
    let list = this.checkList(modification);
    return this.client.put<Modification>(`${this.BASE_URL}/configurator/modifications/${modification.id}/`, {
      name: modification.name, description: modification.description, author_name: modification.author_name,
        likes: modification.likes + 1, housing: list[0], motherboard: list[1], power_supply: list[2],
        cpu: list[3], gpu: list[4], ram: list[5], memory: list[6], cooling: list[7]})
  }
  deleteModification(id:number){
    return this.client.delete<any>(`${this.BASE_URL}/configurator/modifications/${id}/`)
  }
}
