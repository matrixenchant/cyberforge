import { TestBed } from '@angular/core/testing';

import { PcServiceService } from './pc-service.service';

describe('PcServiceService', () => {
  let service: PcServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PcServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
