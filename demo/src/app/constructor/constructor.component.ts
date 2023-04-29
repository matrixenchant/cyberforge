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
  page!:Pagination;
  constructor(public serv:PcServiceService) {
  }
  ngOnInit(){
    this.modifications = this.serv.getListModification();
  }
}
