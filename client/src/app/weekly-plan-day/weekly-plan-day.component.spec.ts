import { ComponentFixture, TestBed } from '@angular/core/testing';

import { WeeklyPlanDayComponent } from './weekly-plan-day.component';

describe('WeeklyPlanDayComponent', () => {
  let component: WeeklyPlanDayComponent;
  let fixture: ComponentFixture<WeeklyPlanDayComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ WeeklyPlanDayComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(WeeklyPlanDayComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
