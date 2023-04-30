import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {catchError, Observable, throwError} from "rxjs";
import {AuthService} from "./auth.service";

@Injectable({
  providedIn: 'root'
})
export class PcServiceService {
  BASE_URL = "http://127.0.0.1:8000"
  constructor(private client:HttpClient, private auth:AuthService) {}
  load:boolean = false;
  getListModification():Observable<Pagination>{
    this.load = true;
    return this.client.get<Pagination>(`${this.BASE_URL}/configurator/modifications/`).pipe(catchError(this.handleError));
  }
  getListPCComponent(type:string):Observable<Pagination>{
    this.load = true;
    return this.client.get<Pagination>(`${this.BASE_URL}/configurator/${type}/`).pipe(catchError(this.handleError));
  }
  getNewPage(url:string):Observable<Pagination>{
    this.load = true;
    return this.client.get<Pagination>(url).pipe(catchError(this.handleError));
  }
  getModification(id:number):Observable<Modification>{
    this.load = true;
    return this.client.get<Modification>(`${this.BASE_URL}/configurator/modifications/${id}/`).pipe(
      catchError(this.handleError))
  }
  getComponent(id:number, type:string):Observable<PCComponent>{
    this.load = true;
    return this.client.get<PCComponent>(`${this.BASE_URL}/configurator/${type}/${id}/`).pipe(
      catchError(this.handleError))
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
          break;
        default:
          console.log(x.type)
      }
    }
    return [housing, motherboard, power_supply, cpu, gpu, ram, memory, cooling]
  }
  addModification(modification:Modification):Observable<Modification>{
    let list = this.checkList(modification);
    return this.client.post<Modification>(`${this.BASE_URL}/configurator/modifications/`, {
      name: modification.name, description: modification.description, author_name: modification.author_name,
      likes: modification.likes, housing: list[0], motherboard: list[1], power_supply: list[2],
      cpu: list[3], gpu: list[4], ram: list[5], memory: list[6], cooling: list[7],}).pipe(catchError(this.handleError))
  }
  updateModification(modification:Modification):Observable<Modification>{
    let list = this.checkList(modification);
    return this.client.put<Modification>(`${this.BASE_URL}/configurator/modifications/${modification.id}/`, {
      name: modification.name, description: modification.description, author_name: modification.author_name,
        likes: modification.likes + 1, housing: list[0], motherboard: list[1], power_supply: list[2],
        cpu: list[3], gpu: list[4], ram: list[5], memory: list[6], cooling: list[7],}).pipe(catchError(this.handleError))
  }
  deleteModification(id:number){
    return this.client.delete<any>(`${this.BASE_URL}/configurator/modifications/${id}/`).pipe(
      catchError(this.handleError))
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
