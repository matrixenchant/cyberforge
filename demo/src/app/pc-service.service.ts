import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {catchError, Observable, throwError} from "rxjs";
import {AuthService} from "./auth.service";

@Injectable({
  providedIn: 'root'
})
export class PcServiceService {

  BASE_URL = 'http://127.0.0.1:8000' //"https://0ad7-95-56-95-4.ngrok-free.app" 'http://127.0.0.1:8000'
  constructor(private client:HttpClient, private auth:AuthService) { }
  load:boolean = false;
  getListModification():Observable<Modification[]>{
    this.load = true;
    return this.client.get<Modification[]>(`${this.BASE_URL}/configurator/modifications/`).pipe(
      catchError(this.handleError))
  }
  getModification(id:number):Observable<Modification>{
    this.load = true;
    return this.client.get<Modification>(`${this.BASE_URL}/configurator/modifications/${id}/`).pipe(
      catchError(this.handleError))
  }
  addModification(modification:Modification):Observable<Modification>{
    let housing, motherboard, power_supply, cpu, gpu, ram, memory, cooling;
    for(let x of modification.components){
      switch (x.type){
        case "housing":
          housing = x.id;
          break;
        case "motherboard":
          motherboard = x.id;
          break;
        case "power_supply":
          power_supply = x.id;
          break;
        case "cpu":
          cpu = x.id;
          break;
        case "gpu":
          gpu = x.id;
          break;
        case "ram":
          ram = x.id;
          break;
        case "memory":
          memory = x.id;
          break;
        case "cooling":
          cooling = x.id;
          break;
      }
    }
    return this.client.post<Modification>(`${this.BASE_URL}/configurator/modifications/`, {
      name: modification.name,
      description: modification.name,
      author_name: modification.author_name,
      likes: modification.likes,
      housing: housing,
      motherboard: motherboard,
      power_supply: power_supply,
      cpu: cpu,
      gpu: gpu,
      ram: ram,
      memory: memory,
      cooling: cooling,})//.pipe(catchError(this.handleError))
  }
  updateModification(modification:Modification, id:number){
    return this.client.put<Modification>(`${this.BASE_URL}/configurator/modifications/${id}/`, modification).pipe(
      catchError(this.handleError))
  }
  deleteModification(id:number){
    return this.client.delete<any>(`${this.BASE_URL}/configurator/modifications/${id}/`).pipe(
      catchError(this.handleError))
  }
  getListCPU():Observable<CPU[]>{
    this.load = true;
    return this.client.get<CPU[]>(`${this.BASE_URL}/configurator/cpu/`)
  }
  getCPU(id:number):Observable<CPU>{
    this.load = true;
    return this.client.get<CPU>(`${this.BASE_URL}/configurator/cpu/${id}/`)
  }
  getListGPU():Observable<GPU[]>{
    this.load = true;
    return this.client.get<GPU[]>(`${this.BASE_URL}/configurator/gpu/`)
  }
  getGPU(id:number):Observable<GPU>{
    this.load = true;
    return this.client.get<GPU>(`${this.BASE_URL}/configurator/gpu/${id}/`)
  }
  getListMotherboard():Observable<Motherboard[]>{
    this.load = true;
    return this.client.get<Motherboard[]>(`${this.BASE_URL}/configurator/motherboard/`)
  }
  getMotherboard(id:number):Observable<Motherboard>{
    this.load = true;
    return this.client.get<Motherboard>(`${this.BASE_URL}/configurator/motherboard/${id}/`)
  }
  getListRAM():Observable<RAM[]>{
    this.load = true;
    return this.client.get<RAM[]>(`${this.BASE_URL}/configurator/ram/`)
  }
  getRAM(id:number):Observable<RAM>{
    this.load = true;
    return this.client.get<RAM>(`${this.BASE_URL}/configurator/ram/${id}/`)
  }
  getListMemory():Observable<Memory[]>{
    this.load = true;
    return this.client.get<Memory[]>(`${this.BASE_URL}/configurator/memory/`)
  }
  getMemory(id:number):Observable<Memory>{
    this.load = true;
    return this.client.get<Memory>(`${this.BASE_URL}/configurator/memory/${id}/`)
  }
  getListCooling():Observable<Cooling[]>{
    this.load = true;
    return this.client.get<Cooling[]>(`${this.BASE_URL}/configurator/cooling/`)
  }
  getCooling(id:number):Observable<Cooling>{
    this.load = true;
    return this.client.get<Cooling>(`${this.BASE_URL}/configurator/cooling/${id}/`)
  }
  getListHousing():Observable<Housing[]>{
    this.load = true;
    return this.client.get<Housing[]>(`${this.BASE_URL}/configurator/housing/`)
  }
  getHousing(id:number):Observable<Housing>{
    this.load = true;
    return this.client.get<Housing>(`${this.BASE_URL}/configurator/housing/${id}/`)
  }
  getListPowerSupplyUnit():Observable<PowerSupplyUnit[]>{
    this.load = true;
    return this.client.get<PowerSupplyUnit[]>(`${this.BASE_URL}/configurator/power_supply_unit/`)
  }
  getPowerSupplyUnit(id:number):Observable<PowerSupplyUnit>{
    this.load = true;
    return this.client.get<PowerSupplyUnit>(`${this.BASE_URL}/configurator/power_supply_unit/${id}/`)
  }


  handleError(error: any) {
    let errorMessage = '';
    localStorage.removeItem('token');
    this.auth.isAuth = false;
    if (error.error instanceof ErrorEvent) {
      // client-side error
      errorMessage = `Error: ${error.error.message}`;
    } else {
      // server-side error
      errorMessage = `Error Code: ${error.status}\nMessage: ${error.message}`;
    }
    console.log(errorMessage);
    return throwError(() => {
      return errorMessage;
    });
  }

}
