import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PcComponentComponent } from './pc-component.component';

describe('PcComponentComponent', () => {
  let component: PcComponentComponent;
  let fixture: ComponentFixture<PcComponentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PcComponentComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PcComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
