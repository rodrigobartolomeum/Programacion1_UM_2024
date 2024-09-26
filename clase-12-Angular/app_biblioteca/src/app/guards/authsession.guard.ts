import { CanActivateFn, Router } from '@angular/router';
import { inject } from '@angular/core';

export const authsessionGuard: CanActivateFn = (route, state) => {

  const router: Router = inject(Router);
  const token = localStorage.getItem('token');
  if(!token) {
    router.navigateByUrl('home');
    return false;
  } else {
    return true;
  }
};
