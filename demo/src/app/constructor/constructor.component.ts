import { Component } from '@angular/core';
import {PcServiceService} from "../pc-service.service";
import {AuthService} from "../auth.service";

@Component({
  selector: 'app-constructor',
  templateUrl: './constructor.component.html',
  styleUrls: ['./constructor.component.css']
})
export class ConstructorComponent {
  modifications!: Modification[];
  currentPage!:Pagination;
  constructor(public serv:PcServiceService) {
  }
  ngOnInit(){
    this.serv.getListModification().subscribe((data) => {
      this.currentPage=data; this.modifications=data.results as Modification[]; this.serv.load = false;});
  }
}
