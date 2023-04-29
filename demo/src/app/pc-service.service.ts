import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {catchError, Observable, throwError} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class PcServiceService {
  BASE_URL = "http://127.0.0.1:8000"
  constructor(private client:HttpClient) { }
  load:boolean = false;
  currentPage!:Pagination;
  getListModification():Observable<Pagination>{
    this.load = true;
    return this.client.get<Pagination>(`${this.BASE_URL}/configurator/modifications/`).pipe(catchError(this.handleError));
  }
  getListPCComponent(type:string):Observable<Pagination>{
    this.load = true;
    return this.client.get<Pagination>(`${this.BASE_URL}/configurator/${type}/`).pipe(catchError(this.handleError));
  }
  getListCooling():Observable<Cooling[]>{
    this.load = true;
    return this.client.get<Cooling[]>(`${this.BASE_URL}/configurator/cooling/`).pipe(catchError(this.handleError));
  }
  getModification(id:number):Observable<Modification>{
    this.load = true;
    return this.client.get<Modification>(`${this.BASE_URL}/configurator/modifications/${id}/`).pipe(
      catchError(this.handleError))
  }
  getComponent(id:number, type:string):Observable<PCComponent>{
    this.load = true;
    return this.client.get<PCComponent>(`${this.BASE_URL}/configurator/${type}/${id}/`)
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
      cooling: cooling,}).pipe(catchError(this.handleError))
  }
  updateModification(modification:Modification, id:number){
    return this.client.put<Modification>(`${this.BASE_URL}/configurator/modifications/${id}/`, modification).pipe(
      catchError(this.handleError))
  }
  deleteModification(id:number){
    return this.client.delete<any>(`${this.BASE_URL}/configurator/modifications/${id}/`).pipe(
      catchError(this.handleError))
  }


  handleError(error: any) {
    let errorMessage = '';
    //localStorage.removeItem('token');
    //this.auth.isAuth = false;
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
